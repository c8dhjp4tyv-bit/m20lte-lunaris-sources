# Lunaris 3.13 for the Samsung Galaxy M20 (m20lte)

Sources for the unofficial Lunaris 3.13 (Android 16) builds of the Galaxy M20 published at
[m20lte-roms](https://github.com/c8dhjp4tyv-bit/m20lte-roms).

The device trees, the 5.10 kernel and the vendor blobs are the public LineageOS ones:

- Device: [android_device_samsung_m20lte](https://github.com/LineageOS/android_device_samsung_m20lte/tree/lineage-24.0), [android_device_samsung_universal7904-common](https://github.com/LineageOS/android_device_samsung_universal7904-common/tree/lineage-24.0)
- Kernel (5.10): [android_kernel_samsung_universal7904](https://github.com/LineageOS/android_kernel_samsung_universal7904/tree/lineage-24.0) (built from `lineage-24.0` on 2026-11-19/20; `58a091089b5a` for Lunaris)
- Vendor: [proprietary_vendor_samsung_m20lte](https://github.com/TheMuppets/proprietary_vendor_samsung_m20lte/tree/lineage-24.0), [proprietary_vendor_samsung_universal7904-common](https://github.com/TheMuppets/proprietary_vendor_samsung_universal7904-common/tree/lineage-24.0)

This repo holds the local manifest and the patches applied on top for Lunaris 3.13.

## Build

```bash
repo init -u https://github.com/Lunaris-AOSP/android -b 16.2 --git-lfs
mkdir -p .repo/local_manifests
cp /path/to/this/repo/local_manifests/m20lte.xml .repo/local_manifests/
repo sync -c -j$(nproc) --force-sync --no-tags
/path/to/this/repo/apply-patches.sh $PWD 
source build/envsetup.sh
lunch lineage_m20lte-bp4a-user
m bacon
```

GMS by default. Vanilla: set `WITH_GMS := false` in `device/samsung/m20lte/lineage_m20lte.mk`. Android 16 has no LineageOS generic IMS, so these builds have no VoLTE.

## Patches

| Path | Patch |
|---|---|
| `device_samsung_m20lte` | m20lte: erofs system (local) |
| `device_samsung_m20lte` | m20lte: Lunaris flags gms=true (local) |
| `device_samsung_m20lte` | m20lte: disable SUW quick start (local) |
| `device_samsung_universal7904-common` | universal7904: Build libhwjpeg with the Samsung legacy |
| `device_samsung_universal7904-common` | universal7904: Link gpsd against the v33 BoringSSL |
| `device_samsung_universal7904-common` | universal7904: Switch to the Python extract-utils |
| `device_samsung_universal7904-common` | universal7904: sepolicy: Use the Lineage libion policy |
| `device_samsung_universal7904-common` | universal7904: Use the exynos7904 platform config again |
| `device_samsung_universal7904-common` | universal7904: generic IMS only if present (A16 local) |
| `device_samsung_universal7904-common` | universal7904: libion sepolicy only if present (A16 |
| `device_samsung_universal7904-common` | universal7904: copy BT/Wi-Fi configs on A16 (local) |
| `hardware_lineage_compat` | compat: Add libssl-v33 |
| `hardware_lineage_compat` | libcomparetf2: Add the remaining long double comparisons |
| `hardware_samsung_slsi-linaro_config` | config: Partially revert "config: Drop support for 4.4 |
| `hardware_samsung_slsi-linaro_config` | config: exynos7885: Switch to the 5.10 kernel |
| `hardware_samsung_slsi-linaro_graphics` | libhwjpeg: Optionally build against Samsung's legacy V4L2 |
| `vendor_pixel_gms` | gms: allow disabling SUW quick start (local) |
