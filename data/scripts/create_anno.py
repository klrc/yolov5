import os


def create_new_labels(src, target, mapper):
    with open(src, "r") as f:
        new_labels = []
        for line in f.readlines():
            c, x, y, w, h = line.strip().split(" ")
            c = int(c)
            if c in mapper:
                c = mapper[c]
                new_labels.append(" ".join([str(c), x, y, w, h]))

    with open(target, "w") as f:
        print(f'processing {src.split("/")[-1]}, found {len(new_labels)} objects')
        for line in new_labels:
            f.write(line + "\n")

def run():
    root = "../datasets/coco"
    # root = '/Volumes/ASM236X/coco'
    mapper = {x: i for i, x in enumerate((0, 1, 2, 3, 5, 7))}

    for src, target in (
        (f"{root}/labels/train2017", f"{root}/labels.c3/train2017"),
        (f"{root}/labels/val2017", f"{root}/labels.c3/val2017"),
    ):
        if not os.path.exists(target):
            os.makedirs(target)

        for fname in os.listdir(src):
            if not fname.startswith("._") and fname.endswith(".txt"):
                create_new_labels(f"{src}/{fname}", f"{target}/{fname}", mapper)

run()