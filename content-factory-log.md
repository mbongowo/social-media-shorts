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

## Batch 19 (2026-08-28)
- CrowdMapAccuracy — Geospatial Data Science — a 2010 comparative study found that OpenStreetMap's crowdsourced road data, built by untrained volunteers, landed within about 6 meters on average of professional Ordnance Survey positions in England, with about 80% motorway overlap between the two datasets. Not a current-events claim, so Gate 1 does not apply. Haklay, M., "How Good is Volunteered Geographical Information? A Comparative Study of OpenStreetMap and Ordnance Survey Datasets," Environment and Planning B: Planning and Design, 37(4):682-703, 2010, DOI 10.1068/b35097. Verification note: this run's network egress proxy again blocked api.crossref.org, journals.sagepub.com, pmc.ncbi.nlm.nih.gov and en.wikipedia.org, so the DOI was cross-checked via two independent WebSearch queries that both returned the same title, author, journal, volume/pages, year, DOI, and the 6m/80% figures, same triangulation fallback used in batches 16-18.
- Rejected concept: Robinson (1950) "Ecological Correlations and the Behavior of Individuals" (the ecological fallacy, state-level vs individual-level correlation between foreign-born status and illiteracy). Rejected for failing Gate 2's accuracy bar, not for lacking a DOI: independent secondary sources disagreed on the actual correlation values (one gave state-level -0.53 vs individual +0.12, another gave state-level +0.53 vs individual -0.11), and the network egress proxy blocked every route to the primary 1950 paper (stats.uwo.ca, pmc.ncbi.nlm.nih.gov, en.wikipedia.org PDF/article mirrors) to resolve the discrepancy. Per Rule Zero, picked a different concept rather than rendering a number that could not be confirmed.

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-08-28)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.

## Batch 20 (2026-08-31)
- RainNowcastVote — GeoAI — DeepMind's deep generative radar model (DGMR) for short-range precipitation nowcasting was judged in a blind evaluation by more than 50 expert meteorologists at the UK Met Office; it was ranked first for accuracy and usefulness in 89% of cases against two competing nowcasting methods, for lead times of 5 to 90 minutes. Not a current-events claim, so Gate 1 does not apply. Ravuri, S., Lenc, K., Willson, M., Kangin, D., Lam, R., Mirowski, P., Fitzsimons, M., Athanassiadou, M., Kashem, S., Madge, S., Prudden, R., Mandhane, A., Clark, A., Brock, A., Simonyan, K., Hadsell, R., Robinson, N., Clancy, E., Arribas, A. and Mohamed, S., "Skilful precipitation nowcasting using deep generative models of radar," Nature 597:672-677, 2021, DOI 10.1038/s41586-021-03854-z. Verification note: this run's network egress proxy again blocked api.crossref.org, nature.com, pubmed, pmc.ncbi.nlm.nih.gov, arxiv.org, semanticscholar.org and deepmind.google (all returned EGRESS_BLOCKED), so the DOI and the 89%/more-than-50-meteorologists figures were cross-checked via four independent WebSearch queries with different phrasings; three of four independently returned the same "89% of cases" / "more than 50 expert meteorologists" / Met Office framing (one paraphrase in the first query hedged toward 88%, and one result blob contained an apparently conflated, unsupported 93% figure alongside the correct 89% figure in the same response; neither of those two outlying mentions was corroborated by any other query, so the well-triangulated 89% figure was used and the outliers discarded), consistent with the DOI-verification fallback used in batches 16-19.

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-08-31)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.

## Batch 21 (2026-09-02)
- LineSimplifyTwins — Maps & Cartography — Urs Ramer (Zurich, Switzerland) published an iterative polygon-approximation algorithm in 1972; David Douglas and Thomas Peucker (Simon Fraser University, Canada) published the identical recursive method in 1973, neither aware of the other's work. The algorithm recursively keeps the point farthest from the straight line between two endpoints and discards every point within a tolerance of that line, repeating until nothing is left to simplify; it remains the default line/polygon generalization algorithm in most GIS software today, commonly called Ramer-Douglas-Peucker. Not a current-events claim, so Gate 1 does not apply. Douglas, D.H. and Peucker, T.K., "Algorithms for the reduction of the number of points required to represent a digitized line or its caricature," Cartographica: The International Journal for Geographic Information and Geovisualization, 10(2):112-122, 1973, DOI 10.3138/FM57-6770-U75U-7727. Corroborating independent-invention source: Ramer, U., "An iterative procedure for the polygonal approximation of plane curves," Computer Graphics and Image Processing, 1(3):244-256, 1972. Verification note: this run's network egress proxy again blocked api.crossref.org (CONNECT tunnel, 403), so the DOI was cross-checked via WebSearch triangulation across the publisher's own listing (utppublishing.com), Google Scholar, Semantic Scholar and ScienceDirect citations, all agreeing on title, full author list, journal, volume/issue/pages, year and DOI; the independent Ramer 1972 fact was separately corroborated via the ESRI GIS Dictionary definition, CRAN package documentation and the original 1972 citation details, same triangulation fallback used in batches 16-20.

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-09-02)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.

## Batch 22 (2026-09-04)
- CornBeltGlow — Remote Sensing explained — satellite-measured chlorophyll fluorescence (solar-induced fluorescence, SIF, a faint light plants emit as a byproduct of photosynthesis) showed the US Corn Belt's photosynthetic signal peaking in July at levels about 40% above the Amazon rainforest's, using GOME-2 satellite data from 2007-2011. Not a current-events claim, so Gate 1 does not apply. Guanter, L., Zhang, Y., Jung, M., Joiner, J., Voigt, M., Berry, J.A., Frankenberg, C., Huete, A.R., Zarco-Tejada, P., Lee, J.E., Moran, M.S., Ponce-Campos, G., Beer, C., Camps-Valls, G., Buchmann, N., Gianelle, D., Klumpp, K., Cescatti, A., Baker, J.M. and Griffis, T.J., "Global and time-resolved monitoring of crop photosynthesis with chlorophyll fluorescence," Proceedings of the National Academy of Sciences USA, 111(14):E1327-E1333, 2014, DOI 10.1073/pnas.1320008111. Verification note: this run's network egress proxy again blocked api.crossref.org (CONNECT tunnel, 403) plus every direct fetch to nasa.gov, jpl.nasa.gov, pubmed, smithsonianmag.com and fondriest.com, so the DOI was cross-checked via WebSearch triangulation across pnas.org, PubMed, the Caltech authors repository and the EU Joint Research Centre repository, all agreeing on title, full author list, journal, volume/pages, year and DOI, same fallback used in batches 16-21. Deliberately framed on screen as a photosynthesis/fluorescence signal, never as "oxygen production": a WebSearch also surfaced a Science Feedback fact-check rating a widely shared "40% more oxygen than the Amazon" paraphrase of this same study as Inaccurate, since the paper measures gross primary productivity via fluorescence, not oxygen output, and never compares annual totals against the Amazon. That mismatch between the viral paraphrase and what the paper actually supports is exactly what Gate 2's "match the claim to the study's scope" rule exists to catch, so the short's hook, fact line and manifest description all use "glow" / photosynthetic signal language and cite the July/GOME-2/2007-2011 scope explicitly.
- Layout note: the first render placed the "+40%" badge overlapping the mid-scene explainer text at the moment the brightest frame was selected for the cover. Fixed by fading the explainer out before the bar chart grows, then re-rendered; confirmed clean in the second cover export.

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-09-04)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.

## Batch 23 (2026-09-07)
- HotspotZTest — Geospatial Data Science — the Getis-Ord Gi* local hotspot statistic only flags a cluster as a genuine hotspot once its z-score passes about 1.96 (95% confidence), meaning under 5% odds the apparent clustering arose from pure chance; this is what separates a statistically significant spatial cluster from a visually dense but random point pattern, and is the exact test behind tools like ArcGIS's Hot Spot Analysis used for real crime, disease and wildfire hotspot maps. Not a current-events claim, so Gate 1 does not apply. Ord, J.K. and Getis, A., "Local Spatial Autocorrelation Statistics: Distributional Issues and an Application," Geographical Analysis, 27(4):286-306, 1995, DOI 10.1111/j.1538-4632.1995.tb00912.x. Verification note: this run's network egress proxy again blocked api.crossref.org (CONNECT tunnel, 403), so the DOI was cross-checked via WebSearch triangulation across Wiley Online Library, the Harvard/Smithsonian ADS abstract service, ResearchGate and Semantic Scholar, all agreeing on title, full author list, journal, volume/pages, year and DOI, same fallback used in batches 16-22. The z=1.96/95%-confidence framing was separately corroborated against Esri's own ArcGIS Pro documentation for the Hot Spot Analysis (Getis-Ord Gi*) tool, the modern implementation of this exact statistic.
- Rejected concept: Chainey, Tompson and Uhlig (2008), "The Utility of Hotspot Mapping for Predicting Spatial Patterns of Crime," Security Journal 21:4-28, DOI 10.1057/palgrave.sj.8350066, comparing kernel density estimation against other hotspot-mapping techniques' accuracy at predicting future crime. The DOI itself triangulated cleanly, but the specific hit-rate / predictive-accuracy-index figures needed for a number-driven hook could not be pinned down: every domain likely to carry the paper's actual result tables (UCL Discovery, OJP, Springer, Tandfonline, ResearchGate) was blocked by this run's network egress proxy, and WebSearch returned only secondary paraphrases describing the methodology, not a matching precise percentage from two independent sources. Per Rule Zero, rejected rather than rendering an approximate or hedged number.

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-09-07)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.

## Batch 24 (2026-09-09)
- RandomFeaturesWin — GeoAI — MOSAIKS uses a bank of fixed, never-optimized random convolutional filters (only a lightweight linear regression on top is trained) and still matches a fully trained ResNet-18 CNN's accuracy across all seven benchmark mapping tasks, training roughly 250 to 10,000x faster (a 2018 MacBook Pro or the same cloud node vs. 7.9 hours per task on an Amazon EC2 p3.xlarge with a Tesla V100 GPU for the CNN). Not a current-events claim, so Gate 1 does not apply. Rolf, E., Proctor, J., Carleton, T., Bolliger, I., Shankar, V., Ishihara, M., Recht, B. and Hsiang, S., "A generalizable and accessible approach to machine learning with global satellite imagery," Nature Communications 12, 4392, 2021, DOI 10.1038/s41467-021-24638-z. Verification note: this run's network egress proxy again blocked api.crossref.org, nature.com, nber.org, researchgate.net and arxiv.org (all EGRESS_BLOCKED or 403), so the DOI, full author list, journal/volume/article number and the seven-task count were cross-checked via the paper's own GitHub code repository README (Global-Policy-Lab/mosaiks-paper), and the specific "250 to 10,000x faster" / "7.9 hours per task" / hardware figures were corroborated by two independent WebSearch queries that both returned the identical detailed sentence, same triangulation fallback used in batches 16-23.
- Theme rotation note: last run (batch 23, 2026-09-07) used Geospatial Data Science, so this run picked GeoAI, the theme least recently used (last seen batch 20, 2026-08-31).

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-09-09)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.

## Batch 25 (2026-09-11)
- ColorBlindMaps — Maps & Cartography — about 8% of men of Northern European descent have red-green color blindness, meaning a standard red-to-green choropleth map is unreadable or badly confused for a large share of male viewers; cartographers address this with tested colorblind-safe diverging palettes (e.g. blue to orange) instead of red to green. Not a current-events claim, so Gate 1 does not apply. Neitz, J. and Neitz, M., "The genetics of normal and defective color vision," Vision Research, 51(7):633-651, 2011, DOI 10.1016/j.visres.2010.12.002, PMID 21167193. Verification note: this run's network egress proxy again blocked api.crossref.org (CONNECT tunnel, 403) plus direct fetches to pubmed.ncbi.nlm.nih.gov and the authors' own neitzvision.com PDF host, so the DOI, title, full author list, journal, volume/pages and year were cross-checked via WebSearch triangulation across the Google Scholar citation record (which itself lists the DOI and PMID), the PubMed listing, Semantic Scholar, and the paper's own hosted PDF mirrors (neitzvision.com and blueconemonochromacy.org), all agreeing; the "about 8%" figure was separately corroborated as specific to men of Northern European descent (not a global figure, avoiding the same scope-mismatch error flagged in the CornBeltGlow batch 22 note) via multiple independent secondary sources on color-vision-deficiency prevalence, same triangulation fallback used in batches 16-24. The cartographic fix (colorblind-safe diverging palettes) is corroborated by Harrower, M. and Brewer, C.A., "ColorBrewer.org: An Online Tool for Selecting Colour Schemes for Maps," The Cartographic Journal, 40(1):27-37, 2003, DOI 10.1179/000870403235002042 (also triangulated via Taylor & Francis, Penn State's institutional repository, Semantic Scholar and ResearchGate), used as supporting context in the short but not as the manifest's source_doi, which cites the core Neitz & Neitz number.
- Cover note: brightest sampled frame (YAVG 48.3 at t=4.0-4.5s) lands mid-scene with the complete hook still on screen plus both the red-green choropleth grid and its colorblind-simulated counterpart fully drawn and legible; after the brightness/contrast/saturation lift the exported cover measures mean luma about 41.7, still under the roughly 57 threshold noted in the brief, so this short will read dimmer than the two best-performing covers in feeds. Flagged plainly in the email.
- Theme rotation note: batches 21-24 ran Maps & Cartography, Remote Sensing explained, Geospatial Data Science, GeoAI in that order, so this run returns to Maps & Cartography.

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-09-11)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.

## Batch 26 (2026-09-14)
- PlanktonMatch — Remote Sensing explained — ocean color satellite data feed the models behind global net primary production (NPP) estimates: marine phytoplankton fix about 48.5 billion tonnes of carbon a year against land plants' 56.4 billion tonnes, a near-even split despite phytoplankton being a tiny fraction of Earth's plant biomass. Not a current-events claim, so Gate 1 does not apply. Field, C.B., Behrenfeld, M.J., Randerson, J.T. and Falkowski, P., "Primary Production of the Biosphere: Integrating Terrestrial and Oceanic Components," Science, 281(5374):237-240, 1998, DOI 10.1126/science.281.5374.237. Verification note: this run's network egress proxy again blocked api.crossref.org (CONNECT tunnel, 403 per the proxy status log), so the DOI was cross-checked via two independent WebSearch queries, one landing directly on the paper's own science.org DOI page and both agreeing on title, full author list, journal, volume/pages, year, DOI and the 104.9 Pg C/yr total NPP split (48.5 ocean / 56.4 land), same triangulation fallback used in batches 16-25. Framed on screen as carbon fixed via ocean-color-derived NPP, not as an oxygen claim, to avoid the same scope-mismatch trap flagged in the CornBeltGlow (batch 22) note, where a popular "40%/50% of Earth's oxygen" paraphrase of similar ocean-productivity science was rated inaccurate by a fact-check because the underlying studies measure carbon fixation/productivity, not net atmospheric oxygen balance.
- Theme rotation note: batch 25 (2026-09-11) used Maps & Cartography (breaking the batches-21-24 rotation to repeat it), so this run picked Remote Sensing explained, the theme least recently used (last seen batch 22, 2026-09-04).
- Frame-zero check: first frame measured mean luma 23.4, std 21.8 (well above zero), with the complete two-line hook fully drawn at t=0; confirmed clean via `self.add(hook)` + `self.wait(1)` opening beat.
- Cover note: brightest sampled frame (YAVG 48.17 at t=8.1-8.4s) lands with the complete hook, both bar values (48.5 / 56.4) and the fact line all fully drawn and legible simultaneously; after the brightness/contrast/saturation lift the exported cover measures mean luma about 41.6, still under the roughly 57 threshold noted in the brief, so this short will read dimmer than the two best-performing covers in feeds. Flagged plainly in the email.

## Note on DoualaSinking.mp4 and PuertoRicoDrought.mp4 (still open, checked again 2026-09-14)
Both still sit at the repo root outside this factory's pipeline (no log entry beyond these notes, no manifest entry, no cover). Left untouched again this run.
