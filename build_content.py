"""
Transforms extracted PPTX content into structured website data.
Copies images to src/assets/images/ and generates src/content/slides.json
with chapter/mineral groupings.
"""
import json
import shutil
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
EXTRACTED = os.path.join(BASE, "pptx_extracted")
SRC_IMAGES = os.path.join(BASE, "src", "assets", "images")
CONTENT_DIR = os.path.join(BASE, "src", "content")
MEDIA_DIR = os.path.join(EXTRACTED, "ppt", "media")

CHAPTERS = [
    {
        "id": "geschichte",
        "title": "Geschichte des Feuersetzens",
        "subtitle": "Eine der ältesten Abbautechniken der Menschheit",
        "slides": list(range(1, 10)),
        "page": "/geschichte",
    },
    {
        "id": "badenweiler",
        "title": "Badenweiler – Geologie & Bergbau",
        "subtitle": "Das Quarzriff am Schwarzwaldrand",
        "slides": list(range(10, 31)),
        "page": "/badenweiler",
    },
    {
        "id": "feuersetzparagenese",
        "title": "Feuersetzparagenese",
        "subtitle": "Die durch Hitze entstandene Mineralvergesellschaftung",
        "slides": list(range(31, 108)),
        "page": "/feuersetzparagenese",
    },
    {
        "id": "begleitende-mineralien",
        "title": "Begleitende Mineralien",
        "subtitle": "Die mineralogische Vielfalt von Badenweiler",
        "slides": list(range(108, 145)),
        "page": "/begleitende-mineralien",
    },
    {
        "id": "museum",
        "title": "Museum & Wanderweg",
        "subtitle": "Badenweiler erleben",
        "slides": list(range(145, 150)),
        "page": "/museum",
    },
]

MINERAL_GROUPS = {
    "feuersetzparagenese": [
        {"id": "entstehung", "name": "Entstehung der Mineralien", "formula": "", "slides": [31]},
        {"id": "geschmolzenes-gestein", "name": "Durch Hitze geschmolzenes Gestein", "formula": "", "slides": [32]},
        {"id": "galenit-elyit", "name": "Galenit mit Elyit und Hydrocerussit", "formula": "", "slides": [33]},
        {"id": "roetliche-quarze", "name": "Durch Hitze rötlich gefärbte Quarze", "formula": "", "slides": [34]},
        {"id": "minium", "name": "Minium (Mennige)", "formula": "Pb₂²⁺Pb⁴⁺O₄", "slides": [35, 36, 37, 38]},
        {"id": "massicotit", "name": "Massicotit", "formula": "PbO", "slides": [39]},
        {"id": "elyit", "name": "Elyit (Leitmineral)", "formula": "Pb₄Cu(SO₄)(OH)₂·O₂·H₂O", "slides": list(range(40, 53))},
        {"id": "elyit-chenit", "name": "Elyit in Umwandlung zu Chenit", "formula": "", "slides": [53, 54, 55]},
        {"id": "chenit", "name": "Chenit", "formula": "Pb₄Cu(SO₄)₂(OH)₆", "slides": [56, 57, 58]},
        {"id": "caledonit", "name": "Caledonit", "formula": "Pb₅Cu₂(OH)₆(CO₃)(SO₄)₃", "slides": [59, 60, 61, 62, 63, 64]},
        {"id": "lithargit", "name": "Lithargit", "formula": "PbO", "slides": [65, 66, 67]},
        {"id": "woodwardit", "name": "Woodwardit", "formula": "Cu₄Al₂(SO₄)(OH)₁₂·2-4H₂O", "slides": [68, 69]},
        {"id": "plattnerit", "name": "Plattnerit", "formula": "PbO₂", "slides": [70, 71]},
        {"id": "elyit-massicotit", "name": "Elyit mit Massicotit", "formula": "", "slides": [72]},
        {"id": "lanarkit", "name": "Lanarkit", "formula": "Pb₂(SO₄)O", "slides": [73, 74, 75, 76]},
        {"id": "steverustit", "name": "Steverustit", "formula": "Pb₁₀Bi₆Fe₂(Si₂O₇)₃O₁₂", "slides": [77]},
        {"id": "hydrocerussit", "name": "Hydrocerussit", "formula": "Pb₃(CO₃)₂(OH)₂", "slides": [78, 79, 80]},
        {"id": "shannonit", "name": "Shannonit", "formula": "Pb₂O(CO₃)", "slides": [81, 82, 83]},
        {"id": "elyit-hydrocerussit-anglesit", "name": "Elyit mit Hydrocerussit und Anglesit", "formula": "", "slides": [84]},
        {"id": "scotlandit", "name": "Scotlandit", "formula": "PbSO₃", "slides": [85, 86]},
        {"id": "nitrobaryt", "name": "Nitrobaryt", "formula": "Ba(NO₃)₂", "slides": [87]},
        {"id": "baryto-anglesit", "name": "Baryto-Anglesit", "formula": "(Ba,Pb)SO₄", "slides": [88]},
        {"id": "al-baryt", "name": "Al-haltiger Baryt", "formula": "BaSO₄", "slides": [89]},
        {"id": "blei-gediegen", "name": "Blei, gediegen", "formula": "Pb", "slides": [90, 91]},
        {"id": "bleinitrat", "name": "Blei-Nitrate", "formula": "Pb₁₃O₈(OH)₆(NO₃)₄ / Pb₂(OH)₃NO₃", "slides": list(range(92, 104))},
        {"id": "anthropogene-mineralien", "name": "Anthropogene Mineralien?", "formula": "", "slides": [104, 105, 106]},
        {"id": "ferrihydrit", "name": "Ferrihydrit", "formula": "Fe₁₀O₁₄(OH)₂", "slides": [107]},
    ],
    "begleitende-mineralien": [
        {"id": "quarz", "name": "Quarz", "formula": "SiO₂", "slides": [108]},
        {"id": "baryt", "name": "Baryt", "formula": "BaSO₄", "slides": [109]},
        {"id": "fluorit", "name": "Fluorit", "formula": "CaF₂", "slides": [110]},
        {"id": "silber", "name": "Silber, gediegen", "formula": "Ag", "slides": [111, 112, 113, 114]},
        {"id": "akanthit", "name": "Akanthit", "formula": "Ag₂S", "slides": [115]},
        {"id": "galenit-schwefel", "name": "Galenit, Zinkblende, Schwefel", "formula": "PbS / ZnS / S", "slides": [116, 117]},
        {"id": "schwefel", "name": "Schwefel, gediegen", "formula": "S", "slides": [118]},
        {"id": "cerussit", "name": "Cerussit", "formula": "PbCO₃", "slides": [119]},
        {"id": "anglesit", "name": "Anglesit", "formula": "PbSO₄", "slides": [120, 121, 122]},
        {"id": "leadhillit-susannit", "name": "Leadhillit / Susannit", "formula": "Pb₄(SO₄)(CO₃)₂(OH)₂", "slides": [123, 124, 125, 126]},
        {"id": "pyromorphit", "name": "Pyromorphit", "formula": "Pb₅(PO₄)₃Cl", "slides": [127, 128, 129]},
        {"id": "mimetesit", "name": "Mimetesit", "formula": "Pb₅(AsO₄)₃Cl", "slides": [130, 131]},
        {"id": "wulfenit", "name": "Wulfenit", "formula": "PbMoO₄", "slides": [132, 133, 134]},
        {"id": "plumbobaryt", "name": "Plumbobaryt", "formula": "(Ba,Pb)SO₄", "slides": [135, 136]},
        {"id": "linarit", "name": "Linarit", "formula": "PbCu(SO₄)(OH)₂", "slides": [137, 138, 139]},
        {"id": "kupfer", "name": "Kupfer, gediegen", "formula": "Cu", "slides": [140]},
        {"id": "langit", "name": "Langit / Posnjakit / Wroewolfeit", "formula": "Cu₄[(OH)₆|SO₄]·2H₂O", "slides": [141, 142, 143, 144]},
    ],
}


def load_slides():
    with open(os.path.join(BASE, "pptx_extracted_content.json"), "r", encoding="utf-8") as f:
        return json.load(f)["slides"]


def copy_images(slides):
    os.makedirs(SRC_IMAGES, exist_ok=True)
    copied = set()
    for s in slides:
        for img in s["images"]:
            if img not in copied:
                src = os.path.join(MEDIA_DIR, img)
                dst = os.path.join(SRC_IMAGES, img)
                if os.path.exists(src) and not os.path.exists(dst):
                    shutil.copy2(src, dst)
                copied.add(img)
    print(f"Copied {len(copied)} images to {SRC_IMAGES}")


def build_structured_content(slides):
    slide_map = {s["number"]: s for s in slides}

    output = {
        "chapters": [],
        "mineral_groups": MINERAL_GROUPS,
    }

    for ch in CHAPTERS:
        chapter_data = {
            "id": ch["id"],
            "title": ch["title"],
            "subtitle": ch["subtitle"],
            "page": ch["page"],
            "slides": [],
        }
        for snum in ch["slides"]:
            if snum in slide_map:
                s = slide_map[snum]
                chapter_data["slides"].append({
                    "number": s["number"],
                    "texts": s["texts"],
                    "notes": s["notes"] or "",
                    "images": s["images"],
                })
        # attach mineral groups if applicable
        if ch["id"] in MINERAL_GROUPS:
            chapter_data["minerals"] = []
            for mg in MINERAL_GROUPS[ch["id"]]:
                mineral_data = {
                    "id": mg["id"],
                    "name": mg["name"],
                    "formula": mg["formula"],
                    "slides": [],
                }
                for snum in mg["slides"]:
                    if snum in slide_map:
                        mineral_data["slides"].append(slide_map[snum])
                chapter_data["minerals"].append(mineral_data)

        output["chapters"].append(chapter_data)

    return output


def main():
    slides = load_slides()
    print(f"Loaded {len(slides)} slides")
    copy_images(slides)
    content = build_structured_content(slides)
    os.makedirs(CONTENT_DIR, exist_ok=True)
    out_path = os.path.join(CONTENT_DIR, "slides.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    print(f"Wrote structured content to {out_path}")
    total_minerals = sum(len(v) for v in MINERAL_GROUPS.values())
    print(f"Chapters: {len(content['chapters'])}, Mineral groups: {total_minerals}")


if __name__ == "__main__":
    main()
