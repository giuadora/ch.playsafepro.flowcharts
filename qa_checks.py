#!/usr/bin/env python3
"""
Quality Assurance Checks for PlaySafePro Flowcharts
Runs automated XML-level checks on both flowchart drawio files.
"""

import xml.etree.ElementTree as ET
import sys
from typing import List, Tuple, Dict, Set
from dataclasses import dataclass

@dataclass
class BoundingBox:
    id: str
    x: float
    y: float
    width: float
    height: float

    def intersects(self, other: 'BoundingBox') -> bool:
        """Check if two bounding boxes overlap."""
        return not (
            self.x + self.width <= other.x or
            other.x + other.width <= self.x or
            self.y + self.height <= other.y or
            other.y + other.height <= self.y
        )

class FlowchartQA:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.tree = ET.parse(filepath)
        self.root = self.tree.getroot()
        self.results: Dict[str, Tuple[bool, str]] = {}

    def get_all_cells(self):
        """Get all mxCell elements from the diagram."""
        return self.root.findall(".//mxCell")

    def qa_02_arrow_connectivity(self) -> Tuple[bool, str]:
        """QA-02: Check that all edges have valid source and target connections."""
        cells = self.get_all_cells()

        # Build set of all vertex IDs
        vertex_ids: Set[str] = set()
        for cell in cells:
            if cell.get('vertex') == '1':
                cell_id = cell.get('id')
                if cell_id:
                    vertex_ids.add(cell_id)

        # Check all edges
        dangling_edges = []
        for cell in cells:
            if cell.get('edge') == '1':
                edge_id = cell.get('id', 'unknown')
                source = cell.get('source')
                target = cell.get('target')

                issues = []
                if not source:
                    issues.append("missing source")
                elif source not in vertex_ids:
                    issues.append(f"source '{source}' not found")

                if not target:
                    issues.append("missing target")
                elif target not in vertex_ids:
                    issues.append(f"target '{target}' not found")

                if issues:
                    dangling_edges.append(f"Edge '{edge_id}': {', '.join(issues)}")

        if dangling_edges:
            return False, f"Found {len(dangling_edges)} dangling edges:\n  " + "\n  ".join(dangling_edges)
        return True, f"All edges properly connected ({len([c for c in cells if c.get('edge') == '1'])} edges checked)"

    def qa_04_node_overlap(self) -> Tuple[bool, str]:
        """QA-04: Check for overlapping nodes."""
        cells = self.get_all_cells()

        # Define elements that are allowed to overlap (header, footer, decorative elements)
        ALLOWED_OVERLAP_IDS = {
            'title', 'subtitle', 'brand',  # Header elements
            'footer-col1', 'footer-col2', 'footer-col3',  # Footer columns
            'FOOTNOTES', 'LEGEND',  # Footer content boxes
            'QR1', 'QR2', 'QR1-label', 'QR2-label',  # QR codes and labels
            'NOTE'  # Inline notes
        }

        # Extract bounding boxes for flow nodes only (not decorative/layout elements)
        bboxes: List[BoundingBox] = []
        for cell in cells:
            if cell.get('vertex') == '1':
                cell_id = cell.get('id', '')
                # Skip root containers (id="0", id="1")
                if cell_id in ['0', '1']:
                    continue

                # Skip allowed overlap elements
                if cell_id in ALLOWED_OVERLAP_IDS:
                    continue

                geometry = cell.find('mxGeometry')
                if geometry is not None:
                    try:
                        x = float(geometry.get('x', 0))
                        y = float(geometry.get('y', 0))
                        width = float(geometry.get('width', 0))
                        height = float(geometry.get('height', 0))

                        # Only check flow nodes (y < 800 excludes footer area)
                        # and nodes with actual dimensions
                        if y < 800 and width > 0 and height > 0:
                            bboxes.append(BoundingBox(cell_id, x, y, width, height))
                    except (ValueError, TypeError):
                        continue

        # Check for overlaps among flow nodes
        overlaps = []
        for i, bbox1 in enumerate(bboxes):
            for bbox2 in bboxes[i+1:]:
                if bbox1.intersects(bbox2):
                    overlaps.append(f"Nodes '{bbox1.id}' and '{bbox2.id}' overlap")

        if overlaps:
            return False, f"Found {len(overlaps)} overlapping flow node pairs:\n  " + "\n  ".join(overlaps)
        return True, f"No overlaps detected ({len(bboxes)} flow nodes checked)"

    def qa_05_footer_check(self) -> Tuple[bool, str]:
        """QA-05: Check for 3-column corporate footer."""
        cells = self.get_all_cells()

        footer_keywords = ['giuadora', 'playsafepro', 'Sonnenstrasse']
        footer_cells = []

        for cell in cells:
            value = cell.get('value', '').lower()
            cell_id = cell.get('id', '')

            # Check if any footer keyword is in the cell value
            for keyword in footer_keywords:
                if keyword.lower() in value:
                    footer_cells.append(cell_id)
                    break

        if len(footer_cells) >= 3:
            return True, f"Footer present with {len(footer_cells)} columns"
        return False, f"Footer incomplete: only {len(footer_cells)} of 3 columns found"

    def qa_06_psp_logo_check(self) -> Tuple[bool, str]:
        """QA-06: Check for PSP logo (image shape with playsafepro URL)."""
        cells = self.get_all_cells()

        logo_found = False
        for cell in cells:
            if cell.get('style', ''):
                style = cell.get('style', '')
                # Check for image shape with playsafepro in URL
                if 'shape=image' in style and 'playsafepro' in style.lower():
                    logo_found = True
                    break

        if logo_found:
            return True, "PSP logo present"
        return False, "PSP logo not found"

    def qa_03_margin_check(self) -> Tuple[bool, str]:
        """QA-03: Check that all nodes maintain minimum margins from page edges."""
        cells = self.get_all_cells()

        # A4 page size in pixels: 794x1123
        PAGE_WIDTH = 794
        PAGE_HEIGHT = 1123
        MIN_MARGIN = 20
        MAX_X = PAGE_WIDTH - MIN_MARGIN
        MAX_Y = PAGE_HEIGHT - MIN_MARGIN

        violations = []

        for cell in cells:
            if cell.get('vertex') == '1':
                cell_id = cell.get('id', '')
                if cell_id in ['0', '1']:
                    continue

                geometry = cell.find('mxGeometry')
                if geometry is not None:
                    try:
                        x = float(geometry.get('x', 0))
                        y = float(geometry.get('y', 0))
                        width = float(geometry.get('width', 0))
                        height = float(geometry.get('height', 0))

                        # Check left/top margin
                        if x < MIN_MARGIN:
                            violations.append(f"Node '{cell_id}' too close to left edge (x={x})")
                        if y < MIN_MARGIN:
                            violations.append(f"Node '{cell_id}' too close to top edge (y={y})")

                        # Check right/bottom margin
                        if x + width > MAX_X:
                            violations.append(f"Node '{cell_id}' extends beyond right margin (x+w={x+width})")
                        if y + height > MAX_Y:
                            violations.append(f"Node '{cell_id}' extends beyond bottom margin (y+h={y+height})")

                    except (ValueError, TypeError):
                        continue

        if violations:
            return False, f"Found {len(violations)} margin violations:\n  " + "\n  ".join(violations)
        return True, "All nodes within page margins"

    def qa_01_center_alignment(self) -> Tuple[bool, str]:
        """QA-01: Check that flow content is horizontally centered on page."""
        cells = self.get_all_cells()

        PAGE_WIDTH = 794
        PAGE_CENTER = PAGE_WIDTH / 2  # 397
        TOLERANCE = 40

        # Collect bounding boxes of flow nodes (y < 800 to exclude footer/footnotes)
        flow_nodes = []

        for cell in cells:
            if cell.get('vertex') == '1':
                cell_id = cell.get('id', '')
                if cell_id in ['0', '1']:
                    continue

                geometry = cell.find('mxGeometry')
                if geometry is not None:
                    try:
                        x = float(geometry.get('x', 0))
                        y = float(geometry.get('y', 0))
                        width = float(geometry.get('width', 0))
                        height = float(geometry.get('height', 0))

                        # Only include flow nodes (above footer area)
                        if y < 800 and width > 0:
                            flow_nodes.append((x, x + width))
                    except (ValueError, TypeError):
                        continue

        if not flow_nodes:
            return False, "No flow nodes found for alignment check"

        # Calculate bounding box of all flow content
        min_x = min(x for x, _ in flow_nodes)
        max_x = max(x_end for _, x_end in flow_nodes)

        # Calculate center of flow content
        content_center = (min_x + max_x) / 2
        offset = abs(content_center - PAGE_CENTER)

        if offset <= TOLERANCE:
            return True, f"Content centered (offset: {offset:.1f}px from center)"
        return False, f"Content not centered: {offset:.1f}px offset (tolerance: {TOLERANCE}px)"

    def run_all_checks(self) -> bool:
        """Run all QA checks and store results."""
        print(f"\nRunning QA checks on: {self.filepath}")
        print("=" * 80)

        checks = [
            ("QA-01: Center Alignment", self.qa_01_center_alignment),
            ("QA-02: Arrow Connectivity", self.qa_02_arrow_connectivity),
            ("QA-03: Margin Check", self.qa_03_margin_check),
            ("QA-04: Node Overlap Check", self.qa_04_node_overlap),
            ("QA-05: Footer Check", self.qa_05_footer_check),
            ("QA-06: PSP Logo Check", self.qa_06_psp_logo_check),
        ]

        all_passed = True
        for check_name, check_func in checks:
            passed, message = check_func()
            self.results[check_name] = (passed, message)

            status = "✓ PASS" if passed else "✗ FAIL"
            print(f"\n{check_name}: {status}")
            print(f"  {message}")

            if not passed:
                all_passed = False

        print("\n" + "=" * 80)
        if all_passed:
            print("✓ ALL CHECKS PASSED")
        else:
            print("✗ SOME CHECKS FAILED")
        print()

        return all_passed

def main():
    """Run QA checks on both flowcharts."""
    files = [
        "Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.drawio",
        "Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.drawio"
    ]

    print("\n" + "=" * 80)
    print("PlaySafePro Flowchart Quality Assurance")
    print("=" * 80)

    all_passed = True
    for filepath in files:
        qa = FlowchartQA(filepath)
        if not qa.run_all_checks():
            all_passed = False

    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    if all_passed:
        print("✓ Both flowcharts passed all quality checks")
        sys.exit(0)
    else:
        print("✗ One or more flowcharts failed quality checks")
        sys.exit(1)

if __name__ == "__main__":
    main()
