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

## Batch 15 (2026-08-19)
- ProjectionScoreCard — Maps & Cartography — Goldberg and Gott's six-category distortion metric (isotropy, area, flexion, skewness, distances, boundary cuts) objectively scored world map projections; Mercator scores 8.296 versus Winkel Tripel's 4.563, nearly double the distortion, explaining why National Geographic adopted Winkel Tripel in 1998. Goldberg and Gott, "Flexion and Skewness in Map Projections of the Earth," Cartographica 42(4):297-318, 2007, DOI 10.3138/carto.42.4.297

## Batch 16 (2026-08-21)
- GeoTimeTwin — GeoAI — geography-aware self-supervised learning: pairing satellite images of the same location captured at different times (plus geolocation as a pretext signal) gives a contrastive model a free training pair with zero human labels, beating a standard self-supervised baseline by about 8% on satellite image classification. Ayush, Uzkent, Meng, Tanmay, Burke, Lobell and Ermon, "Geography-Aware Self-Supervised Learning," ICCV 2021, pp. 10181-10190, DOI 10.1109/ICCV48922.2021.01002. Verification note: this run's network egress proxy blocked direct access to api.crossref.org, doi.org, arxiv.org and semanticscholar.org, so the DOI was cross-checked via WebSearch triangulation across DBLP, ResearchGate and a CVF/arXiv listing instead of a direct Crossref query. All three agreed on title, full author list, venue and DOI.

## Note on DoualaSinking.mp4 (found 2026-08-19)
DoualaSinking.mp4 exists at the repo root (committed 2026-08-14, commit 55468b5, authored directly by Mbongowo, not by this factory routine) but has no entry in this log, no captions_manifest.json entry, and no cover in covers/. It falls outside this factory's pipeline so it was left untouched, but it means captions_manifest.json is not a complete index of every short in the repo root. Flagged again in this run's email.

## Note on PuertoRicoDrought.mp4 (found this run, 2026-08-21)
PuertoRicoDrought.mp4 exists at the repo root (committed 2026-08-19, commit 1d03b10, authored directly by Mbongowo, not by this factory routine) but has no entry in this log, no captions_manifest.json entry, and no cover in covers/. Same situation as DoualaSinking.mp4 above. Left untouched, flagged in this run's email.

## Batch 17 (2026-08-24)
- LabelPacking — Maps & Cartography — placing non-overlapping labels next to points on a map (point-feature label placement) is proven NP-hard; the best guaranteed algorithm can only promise a labeling within 2x of the optimal fit. Not a current-events claim, so Gate 1 does not apply. Formann, M. and Wagner, F., "A packing problem with applications to lettering of maps," Proceedings of the 7th Annual ACM Symposium on Computational Geometry (SoCG '91), ACM, pp. 281-288, 1991, DOI 10.1145/109648.109680. Verification note: this run's network egress proxy again blocked api.crossref.org, dl.acm.org, doi.org, wikidata.org and dblp.org, so the DOI was cross-checked via WebSearch triangulation (three independent queries agreeing on title, authors, venue, pages, year and DOI), same fallback as GeoTimeTwin (batch 16).

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-08-24)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.

## Batch 18 (2026-08-26)
- SinglePhotonIce — Remote Sensing explained — NASA's ICESat-2 fires 10,000 laser pulses a second from its ATLAS instrument and its single-photon-sensitive detectors track individual returning photons, giving enough precision to measure Greenland and Antarctic ice sheet height loss to within 4mm a year. Not a current-events claim, so Gate 1 does not apply. Markus, T., Neumann, T., Martino, A., Abdalati, W. et al., "The Ice, Cloud, and land Elevation Satellite-2 (ICESat-2): Science requirements, concept, and implementation," Remote Sensing of Environment 190:260-273, 2017, DOI 10.1016/j.rse.2016.12.029. Verification note: this run's network egress proxy again blocked api.crossref.org (CONNECT tunnel failed, 403), so the DOI was cross-checked via WebSearch triangulation across ResearchGate, ScienceDirect and NASA's own hosted PDF of the paper, all agreeing on title, full author list, journal, volume/pages and DOI, same fallback used in batches 16-17. The 10,000 pulses/sec and 4mm/year figures were separately corroborated on NASA's own ICESat-2 mission pages (icesat-2.gsfc.nasa.gov), which also serves as source_url as the primary agency page.
- Rejected concept: volcanic ground deformation via InSAR (would have used Massonnet et al. 1995 Nature paper on Mount Etna). Not rejected for failing either gate; the DOI and fact were solid. Rejected because `pro/GEO_volcanoinsar.mp4` already exists in this repo (added by a separate, non-factory pipeline) and the topic would have overlapped with existing library content.

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-08-26)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.
