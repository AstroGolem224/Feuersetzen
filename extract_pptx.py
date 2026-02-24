import xml.etree.ElementTree as ET
import json
import os

base = r'c:\Users\matth\OneDrive\Dokumente\GitHub\Projekt_Eight\learn-ai\pptx_extracted'
out_path = r'c:\Users\matth\OneDrive\Dokumente\GitHub\Projekt_Eight\learn-ai\pptx_extracted_content.json'
slides_dir = os.path.join(base, 'ppt', 'slides')
notes_dir = os.path.join(base, 'ppt', 'notesSlides')
rels_dir = os.path.join(slides_dir, '_rels')

a_ns = '{http://schemas.openxmlformats.org/drawingml/2006/main}t'
img_exts = ('.jpeg','.jpg','.png','.gif','.bmp','.tiff','.svg','.emf','.wmf')

result = {'slides': []}

for i in range(1, 150):
    slide_data = {'number': i, 'texts': [], 'notes': '', 'images': []}

    slide_path = os.path.join(slides_dir, 'slide{}.xml'.format(i))
    if os.path.exists(slide_path):
        tree = ET.parse(slide_path)
        for t in tree.iter(a_ns):
            if t.text:
                slide_data['texts'].append(t.text)

    notes_path = os.path.join(notes_dir, 'notesSlide{}.xml'.format(i))
    if os.path.exists(notes_path):
        tree = ET.parse(notes_path)
        parts = []
        for t in tree.iter(a_ns):
            if t.text:
                parts.append(t.text)
        slide_data['notes'] = ' '.join(parts)

    rels_path = os.path.join(rels_dir, 'slide{}.xml.rels'.format(i))
    if os.path.exists(rels_path):
        tree = ET.parse(rels_path)
        root = tree.getroot()
        for rel in root:
            target = rel.get('Target', '')
            if target.lower().endswith(img_exts):
                slide_data['images'].append(os.path.basename(target))

    result['slides'].append(slide_data)

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

count = len(result['slides'])
print('Done. {} slides written to {}'.format(count, out_path))
