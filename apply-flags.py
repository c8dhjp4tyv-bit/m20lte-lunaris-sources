import sys
gms = sys.argv[1] if len(sys.argv) > 1 else "true"
p = "lineage_m20lte.mk"
s = open(p).read()
start = s.find("\n# Lunaris\n")
if start != -1:
    s = s[:start] + "\n"
s = s.rstrip("\n") + f'''

# Lunaris
WITH_GMS := {gms}
WITH_GMS_COMMS_SUITE := false
WITH_PIXEL_LAUNCHER := false
TARGET_USE_MAPS := false
TARGET_USE_GPHOTOS := false
TARGET_USE_WALLPAPERS := false
PRODUCT_SYSTEM_PROPERTIES += ro.lunaris.maintainer=umutcagand
'''
open(p, "w").write(s)
