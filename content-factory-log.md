# Content Factory Log

Master list of every short concept ever produced. Never repeat a concept below.

## Batch 1-4 (pre-existing)
- NDVIShort — Remote Sensing explained
- FreeDataShort — Geospatial Data Science
- RedRiverNorth — Maps & Cartography
- MercatorLie — Maps & Cartography
- SARClouds — Remote Sensing explained
- AICantSaveYou — GeoAI
- DroughtEarly — Remote Sensing explained
- ClinicAccess — Geospatial Data Science
- UrbanHeat — Remote Sensing explained
- GPSTrilateration — Geospatial Data Science
- NightLights — Remote Sensing explained
- PixelTruth — Remote Sensing explained
- RiversMove — Maps & Cartography
- SaharaAmazon — Remote Sensing explained
- AICRSBug — GeoAI
- AISAMBuildings — GeoAI
- STACSearch — Geospatial Data Science
- COGStream — Geospatial Data Science
- FlashFloodSeason — Remote Sensing explained
- FloodMapping — Remote Sensing explained
- HeatAttribution — Remote Sensing explained
- NISARWatch — Remote Sensing explained

## Batch 5 (2026-07-31)
- RadarBackscatter — Remote Sensing explained — SAR backscatter: rough surfaces scatter bright, smooth surfaces bounce away dark
- SpectralFingerprint — Remote Sensing explained — every material has a distinct reflectance curve across bands
- ContourSlope — Maps & Cartography — contour line spacing encodes slope steepness
- FoundationModel — GeoAI — geospatial foundation models pretrain on unlabeled imagery, fine-tune with few labels
- MAUP — Geospatial Data Science — Modifiable Areal Unit Problem: aggregation boundary choice can flip conclusions
- SpatialAutocorrelation — Geospatial Data Science — Tobler's First Law and spatial data leakage in ML

## Batch 6 (2026-08-01)
- ResolutionTradeoff — Remote Sensing explained — spatial resolution vs revisit time tradeoff (Landsat vs weather satellites)
- AtmosphereBlur — Remote Sensing explained — atmospheric correction: sunlight scatters/absorbs through the atmosphere twice before reaching the sensor
- CoastlineParadox — Maps & Cartography — measured coastline length grows without limit as ruler size shrinks (fractal geometry)
- DomainShift — GeoAI — models trained on one region/sensor lose accuracy when applied elsewhere without adaptation
- VectorRaster — Geospatial Data Science — vector (points/lines/polygons) vs raster (grid of cells) data models
- KrigingGuess — Geospatial Data Science — kriging spatial interpolation estimates unsampled values by distance-weighted correlation

## Batch 7 (2026-08-02)
- SunSyncOrbit — Remote Sensing explained — sun-synchronous orbit keeps satellites crossing the equator at a consistent local time for comparable lighting
- BitDepthSecret — Remote Sensing explained — radiometric resolution: Landsat 8 records 12-bit (4096 levels) vs an 8-bit photo's 256
- ClassBreaksLie — Maps & Cartography — choropleth classification method (equal interval, quantile, natural breaks) changes a map's visual story from the same data
- ImageChipping — GeoAI — large satellite scenes are cut into small tiles (chips) for neural network training, then stitched back together
- RareClassTrap — Geospatial Data Science — class imbalance: rare-event models (e.g. flood pixels) can score high accuracy while missing every positive case
- QuadtreeIndex — Geospatial Data Science — spatial indexes (quadtree, R-tree) split space into nested boxes so nearest-neighbor queries skip most of the data

## Batch 8 (2026-08-03)
- TerrainLean — Remote Sensing explained — orthorectification: off-nadir viewing angles make tall terrain lean sideways in raw satellite imagery until elevation data warps it back to its true map position
- FalseColorVeg — Remote Sensing explained — false color composites remap near-infrared reflectance into the red channel, making healthy chlorophyll-rich vegetation glow bright red
- GreatCircleLie — Maps & Cartography — a straight line on a Mercator map is a constant-bearing rhumb line, not the shortest path; the true shortest path on a sphere is a curved great circle
- ShortcutLearning — GeoAI — shortcut learning: a model can hit high accuracy by latching onto an easy correlated feature (e.g. a fence pattern) instead of the true target, then fail when that shortcut is absent
- HexGridEdge — Geospatial Data Science — hexagonal spatial indexes (e.g. H3) give every neighboring cell equal distance, unlike square grids where diagonal neighbors sit farther away than orthogonal ones
- GPSSnap — Geospatial Data Science — map matching algorithms snap noisy raw GPS fixes onto the most probable road segment using the road network's topology

## Batch 9 (2026-08-05)
- TissotCircles — Maps & Cartography — Tissot's Indicatrix: identical circles placed across the globe swell into differently-sized ellipses once projected flat, revealing exactly where and how much a projection distorts area

## Batch 10 (2026-08-07)
- SuperResHallucination — GeoAI — AI super-resolution models pattern-complete missing detail; trained on natural photos, they can hallucinate plausible-looking roads or buildings that were never in the real satellite scene

## Batch 11 (2026-08-10)
- FourColorMap — Maps & Cartography — the Four Color Theorem: any flat map can be colored with just 4 colors so no two touching regions match; proven in 1976 by Appel & Haken, the first major theorem verified with substantial computer assistance

## Batch 12 (2026-08-12)
- OnboardCloudFilter — GeoAI — ESA's Phi-sat-1 ran an onboard neural net (CloudScout) that screened images for cloud cover and discarded unusable ones before downlink to the ground

## Batch 13 (2026-08-14)
- CartogramBend — Maps & Cartography — a diffusion-based cartogram algorithm resizes map regions by population instead of land area, treating population like a gas that spreads to equal density and dragging borders along with it. Gastner and Newman, "Diffusion-based method for producing density-equalizing maps," PNAS 101(20), 2004, DOI 10.1073/pnas.0400280101

## Batch 14 (2026-08-17)
- PovertyFromSpace — GeoAI — a CNN trained via transfer learning uses nighttime light brightness as a noisy wealth proxy to learn image features from daytime satellite photos, then estimates local household consumption and asset wealth, explaining up to 75% of local economic variation across five African countries (Nigeria, Tanzania, Uganda, Malawi, Rwanda) without any household survey. Jean, Burke, Xie, Davis, Lobell and Ermon, "Combining satellite imagery and machine learning to predict poverty," Science 353(6301):790-794, 2016, DOI 10.1126/science.aaf7894
