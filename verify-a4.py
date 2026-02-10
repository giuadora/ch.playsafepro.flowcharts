#!/usr/bin/env python3
"""Verify that all SVG elements fit within A4 pixel bounds (794 x 1123 px)."""

import sys
import re
import xml.etree.ElementTree as ET

A4_W = 794
A4_H = 1123
TOLERANCE = 0.5  # sub-pixel tolerance

NS = {"svg": "http://www.w3.org/2000/svg", "xlink": "http://www.w3.org/1999/xlink"}


def parse_transform(attr):
    """Extract translate(tx,ty) and scale(s) from a transform attribute."""
    tx, ty, sx, sy = 0, 0, 1, 1
    if not attr:
        return tx, ty, sx, sy
    m = re.search(r"translate\(\s*([-\d.]+)[,\s]+([-\d.]+)\s*\)", attr)
    if m:
        tx, ty = float(m.group(1)), float(m.group(2))
    m = re.search(r"scale\(\s*([-\d.]+)(?:[,\s]+([-\d.]+))?\s*\)", attr)
    if m:
        sx = float(m.group(1))
        sy = float(m.group(2)) if m.group(2) else sx
    return tx, ty, sx, sy


def apply_transform(bbox, tx, ty, sx, sy):
    """Apply translate+scale to a bounding box (x, y, w, h) -> (ax, ay, aw, ah)."""
    x, y, w, h = bbox
    return (x * sx + tx, y * sy + ty, w * sx, h * sy)


def element_tag(elem):
    """Return local tag name without namespace."""
    return elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag


def get_bbox(elem):
    """Return (x, y, w, h) bounding box for a shape element, or None."""
    tag = element_tag(elem)
    a = elem.attrib

    if tag == "rect":
        if all(k in a for k in ("x", "y", "width", "height")):
            return (float(a["x"]), float(a["y"]), float(a["width"]), float(a["height"]))

    elif tag == "polygon":
        pts_str = a.get("points", "")
        nums = list(map(float, re.findall(r"[-\d.]+", pts_str)))
        xs = nums[0::2]
        ys = nums[1::2]
        if xs and ys:
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)
            return (min_x, min_y, max_x - min_x, max_y - min_y)

    elif tag == "line":
        if all(k in a for k in ("x1", "y1", "x2", "y2")):
            x1, y1, x2, y2 = float(a["x1"]), float(a["y1"]), float(a["x2"]), float(a["y2"])
            return (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

    elif tag == "path":
        d = a.get("d", "")
        nums = list(map(float, re.findall(r"[-+]?\d*\.?\d+", d)))
        # path coordinates come in pairs
        xs = nums[0::2]
        ys = nums[1::2]
        if xs and ys:
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)
            return (min_x, min_y, max_x - min_x, max_y - min_y)

    elif tag == "image":
        if all(k in a for k in ("x", "y", "width", "height")):
            return (float(a["x"]), float(a["y"]), float(a["width"]), float(a["height"]))

    elif tag == "text":
        x_val = float(a.get("x", 0))
        y_val = float(a.get("y", 0))
        # text bounding box is approximate; just check anchor point
        return (x_val, y_val, 0, 0)

    return None


def check_bounds(ax, ay, aw, ah):
    """Return True if the absolute bbox fits within A4 bounds (with tolerance)."""
    return (
        ax >= -TOLERANCE
        and ay >= -TOLERANCE
        and ax + aw <= A4_W + TOLERANCE
        and ay + ah <= A4_H + TOLERANCE
    )


def walk(elem, parent_tx=0, parent_ty=0, parent_sx=1, parent_sy=1):
    """Walk the SVG tree; yield (elem, absolute_bbox) for every element with geometry."""
    tag = element_tag(elem)

    tx, ty, sx, sy = parse_transform(elem.attrib.get("transform"))
    # compose with parent
    abs_tx = parent_tx + tx * parent_sx
    abs_ty = parent_ty + ty * parent_sy
    abs_sx = parent_sx * sx
    abs_sy = parent_sy * sy

    bbox = get_bbox(elem)
    if bbox is not None and tag != "text":
        ab = apply_transform(bbox, abs_tx, abs_ty, abs_sx, abs_sy)
        yield (elem, ab)

    for child in elem:
        if tag == "g":
            yield from walk(child, abs_tx, abs_ty, abs_sx, abs_sy)
        else:
            yield from walk(child, parent_tx, parent_ty, parent_sx, parent_sy)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 verify-a4.py <file.svg>")
        sys.exit(2)

    path = sys.argv[1]
    tree = ET.parse(path)
    root = tree.getroot()

    # Check root dimensions
    w = root.attrib.get("width", "")
    h = root.attrib.get("height", "")
    errors = []

    if w != str(A4_W) or h != str(A4_H):
        errors.append(f"SVG root size is {w}x{h}, expected {A4_W}x{A4_H}")

    # Walk all elements
    for elem, (ax, ay, aw, ah) in walk(root):
        if not check_bounds(ax, ay, aw, ah):
            eid = elem.attrib.get("id", element_tag(elem))
            errors.append(
                f"  OUT OF BOUNDS: <{element_tag(elem)}> id=\"{eid}\" "
                f"abs bbox=({ax:.1f}, {ay:.1f}, {aw:.1f}, {ah:.1f}) "
                f"exceeds {A4_W}x{A4_H}"
            )

    if errors:
        print(f"FAIL — {len(errors)} issue(s) found:")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print(f"PASS — all elements within {A4_W}x{A4_H} A4 bounds.")
        sys.exit(0)


if __name__ == "__main__":
    main()
