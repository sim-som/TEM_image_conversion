#!python
#%%
from skimage import io
import mrcfile
from pathlib import Path
import argparse
# %%

def convert_tiff_to_mrc(tiff_file_path):

    print(f"Converting {tiff_file_path.name} to mrc ...")

    img_data = io.imread(tiff_file_path)

    mrc_file_dest = tiff_file_path.parent / Path(f"{tiff_file_path.stem}.mrc")

    print(f"Saving converted mrc in same directory: {mrc_file_dest} ...")
    with mrcfile.new(mrc_file_dest) as mrc:
        mrc.set_data(img_data)


# %%
parser = argparse.ArgumentParser(
    description="Command line TIFF to MRC converter (recursive)"
)

parser.add_argument("tiff_dir")
parser.add_argument("--wildcard")
parser.add_argument(
    "-r", "--recursive",
    action="store_true"
)

args = parser.parse_args()
tiff_dir = Path(args.tiff_dir)
assert tiff_dir.exists() and tiff_dir.is_dir()

if args.wildcard:
    wildcard = args.wildcard
else:
    wildcard = "*.tiff"

if args.recursive:
    tiff_files = list(tiff_dir.rglob(wildcard))
else:
    tiff_files = list(tiff_dir.glob(wildcard))

assert len(tiff_files) > 0

for tiff_file in tiff_files:
    convert_tiff_to_mrc(tiff_file)



