# ANSHUMAN — media generation prompt pack

Every image and video on the site can be regenerated with AI using **your face**.
This file gives the exact flow + one copy-paste prompt per asset, matched to the
real look of each shipped scene.

**Style constants** — append to the end of every prompt:

> Cinematic 35mm anamorphic film still, heavy fine film grain, deep matte blacks,
> chiaroscuro lighting, muted palette of black + crimson red + warm amber,
> photorealistic, no watermark, no border, no extra text.

**Wardrobe constants** — the same person in every asset:

> a young Indian man, medium wavy dark hair, light stubble, tailored black suit
> over a black shirt, black leather shoes (add dark sunglasses in noir scenes).

`[YOUR FACE]` means: attach your face photo as the tool's face/character
reference (see the flow below).

---

## 0. The flow — putting YOUR face in every video & image

1. **Pick one anchor face photo.** Front-facing, even light, no glasses,
   neutral expression. This one photo becomes the identity reference for
   *everything*.
2. **Make an identity anchor still (images).** In any generator that accepts a
   face reference (Midjourney `--cref`, GPT-image / Nano Banana edit,
   Flux/SD face-swap), generate the still below and instruct:
   *"the man has exactly the face from my reference photo, same identity,
   keep everything else in the image identical."*
3. **Face → video.** Feed the anchor still as the **first frame** + your face
   photo as **face/character reference** into an image-to-video model
   (Veo 3.1, Kling 2.1 Master, Runway Gen-4, Sora). First-frame control is what
   keeps the body, suit and framing identical across clips.
4. **Keep one seed/reference bundle.** Reuse the same face ref + wardrobe
   constants for every generation so scene 1, 2, 4, 5, 6 all show the same man.
5. **Drop files into the paths in the table below**, then rebuild the media
   pipeline for the hero clip:
   `python tools/build_media.py && python tools/track.py`.

---

## 1. Asset map

| Asset on site | File to replace | Type | Specs |
|---|---|---|---|
| Scene 1 walking man (transparent video) | `assets_src/v1.mp4` | video | 9:16 720×1280, 24fps, ~10s, **white backdrop** |
| Scene 1 letter surface texture | `assets_src/ref_typo.jpg` | image | red word on black |
| Scene 2 film loop | `section 2 refrence video.mp4` (→ `public/media/universe.mp4`) | video | 16:9, ~10s seamless loop |
| Scene 2 tool cubes (parked variant) | `public/tools/*.png` | image | cube on black |
| Scene 3 year cards | `public/years/2021.jpg … 2026.jpg` | image | ~264×150-200 |
| Scene 3 standing figure | `public/years/figure.png` | image | 123×317 |
| Scene 4 room backdrop | `public/projects/plate.jpg` | image | 1600×900 |
| Scene 4 centre figure | `public/projects/person.png` | image | 160×335 |
| Scene 4 project cards | `public/projects/p01_timeless.png … p12_steps.png` | image | 16:10 web cards |
| Scene 6 finale backdrop | `public/fin/plate.jpg` | image | 1600×900 |
| Scene 6 finale man cut-out | `public/fin/man.png` | image | 450×730, alpha |
| Footer second still | `footer 2nd image.jpg` (probed as frame 2) | image | 16:9 |
| Certifications reference | `section 5 main refrence.jpg` (style ref) | image | 16:9 |

---

## 2. Video prompts

### V1 — hero walking clip → `assets_src/v1.mp4`  *(the one that matters most)*

The site removes the backdrop **offline** (`tools/matte.py`), so the footage
**must be shot on a bright white backdrop** — not black.

> **Prompt:** Vertical 9:16, 10 seconds. [YOUR FACE] A young Indian man in a
> tailored black suit walks slowly and confidently straight toward the camera,
> starting small in frame and ending about 80% of frame height. Pure WHITE
> seamless studio cyclorama behind him, bright even shadowless white lighting,
> subject evenly lit, full body visible and centred the whole time. Static
> locked camera, no zoom, no cuts, no props, no text. Calm steady stride,
> relaxed arms. End pose nearly matches start pose so the clip loops.
> Photorealistic, natural skin texture.

Pipeline after saving: `python tools/build_media.py && python tools/track.py`
(regenerates `public/media/hero.mp4/.webm/.jpg` + the per-frame foot tracking).

### V2 — scene 2 universe film → `section 2 refrence video.mp4`

> **Prompt:** 16:9, 10-second seamless loop. Seen from behind, [YOUR FACE
> identity] a man in a black suit stands centred in a vast black void, head
> tilted slightly up. Around him, glossy black 3D cubes drift and rotate very
> slowly, each face glowing with an app logo: Figma, Photoshop "Ps", After
> Effects "Ae", Premiere "Pr", Lightroom "Lr", Notion, Claude, ChatGPT,
> Midjourney, Spline, Framer, Webflow. Thin red neon light arcs orbit behind
> him; the black wet floor mirrors the red glow. Extremely slow dolly drift,
> volumetric black fog. Final frame matches the first frame perfectly for a
> hidden loop. Dark, moody, cinematic.

### V3 — certifications noir walk (reference for a future scene) → style ref only

> **Prompt:** 16:9 noir film still. [YOUR FACE] A man in a black suit and dark
> sunglasses, black tie blown sideways, walks toward camera on rain-wet asphalt
> in cold teal-cyan fog, a cigarette at his lips with a thin smoke trail
> (replace with a toothpick if the tool refuses smoking). Frosted-glass cards
> float beside him: Figma "UI/UX Design Essentials", Google "Foundations of
> Digital Marketing", Adobe "Photoshop", freeCodeCamp "Responsive Web Design",
> Meta "Front-End Developer", each stamped CERTIFIED with a year. Giant white
> condensed type "CERTIFICATIONS" on the left. Teal-black palette, cinematic.

---

## 3. Image prompts

### I1 — wordmark artwork → `assets_src/ref_typo.jpg` (and any `Gireesh typo.jpg`-style art)

> **Prompt:** Pure black background. The word "ANSHUMAN" in an ultra-condensed
> heavy grotesque uppercase (Anton style), vivid crimson red #d61f1f, filling
> 95% of the frame edge to edge, letters almost touching. The red ink carries a
> heavily distressed painted texture: hairline scratches, specks, abrasions and
> uneven ink like a worn screen print. Nothing else in frame, no glow.
> *(The site extracts the scratch surface from this image; keep the lettering
> solid red on pure black.)*

### I2 — hero composite reference → `main refrence.jpg` style (site draws it live; art is a style ref)

> **Prompt:** Pure black poster. The red distressed word "ANSHUMAN" edge to
> edge; small white condensed caption "•••WELCOME TO MY WORLD•••" centred above
> it; a white chip "•LEGEND•" over the top-right letter; a white chip
> "•ARTIST ANSHUMAN•" over the bottom-left letter; six small white
> right-pointing triangles stacked on the left and right edges; a 3×10 grid of
> white dots top-left and bottom-right.

### I3 — scene 3 year cards → `public/years/2021.jpg … 2026.jpg`

Common: *small 3:2-ish documentary photograph, grainy, sepia/monochrome.*

- **2021:** a humble cluttered beginner desk, old laptop, notebooks, one lamp — monochrome sepia.
- **2022:** two laptops side by side covered in design sketches and sticky notes — monochrome.
- **2023:** a monitor glowing with design software on a tidy desk — monochrome.
- **2024:** silhouette of a man working late at his desk, lit only by the screen — monochrome.
- **2025:** a video-editing suite, timeline glowing on a big monitor — monochrome.
- **2026:** the man seen from behind looking at a city skyline at sunrise — warm amber duotone.

### I4 — scene 3 figure → `public/years/figure.png`

> **Prompt:** Full-body back view of [YOUR FACE identity] a man in a black suit
> standing still, warm amber rim light on his shoulders, isolated on pure
> black, tall 1:2.6 crop.

### I5 — scene 4 room plate → `public/projects/plate.jpg` (1600×900)

> **Prompt:** Vast pitch-black circular amphitheatre. Centre: back view of a
> man in a black suit ([YOUR FACE identity]) standing on a wet reflective black
> floor marked with two glowing concentric circles. Around him, twelve large
> glowing screens hang tilted inward in two curved cinema rows, each showing a
> different dark minimal website, rimmed in red, amber, white and green light.
> A huge dark ceiling ring above emits a soft white halo and thin volumetric
> light shafts onto the man. Photorealistic cinematic still, deep blacks.

### I6 — scene 4 figure → `public/projects/person.png`

> **Prompt:** Back view, man in a black suit standing, hands relaxed at his
> sides, full body, warm red rim light tracing his silhouette, isolated on
> pure black, vertical 1:2.

### I7 — the twelve project cards → `public/projects/p01…p12`

Common: *dark premium website hero card, tiny sans UI chrome along the top,
16:10, elegant white serif headline.*

- **p01 Timeless Experiences:** monochrome cinematic shot of a hooded man from behind in a rainy night city.
- **p02 More Than A Game:** a matte black game controller floating on charcoal grey, one red accent dot.
- **p03 Build Without Limits:** a huge red-and-black planet limb rising behind the serif title on black.
- **p04 Driven by Better Design:** rear three-quarter of a black sports car, amber tail lights glowing, night.
- **p05 Your Ideas In Motion:** flowing molten-amber silk ribbons swirling on black.
- **p06 Sound & Second Motion:** a dancer mid-motion with long light-trail motion blur on a dark stage.
- **p07 Good Food Brighter Moods:** top-down vibrant salad bowl on a dark red backdrop.
- **p08 Travel Explore Belong:** a dramatic snow mountain peak under a stormy blue sky.
- **p09 Find Your Space:** a minimal warm interior, single armchair and floor lamp, soft light.
- **p10 Play Create Repeat:** portrait of a young man lit by a glowing orange ring light, black backdrop.
- **p11 Designing A Cleaner Tomorrow:** wind turbines on green hills at dusk, muted green duotone.
- **p12 Small Steps Big Change:** macro monstera leaves with water droplets on black.

### I8 — finale plate → `public/fin/plate.jpg`

> **Prompt:** A monumental condensed sans-serif word "ANSHUMAN" in off-white at
> the top fading into deep red at the bottom, rising out of swirling red smoke
> and black fog, filling a 16:9 frame like a movie title. Grainy, photographic,
> no person in frame (the man is a separate layer).

### I9 — finale man cut-out → `public/fin/man.png`

> **Prompt:** [YOUR FACE] A man with wavy dark hair and dark sunglasses in a
> black suit, three-quarter view, one hand raising a lit cigarette to his lips
> with a thin smoke trail (or hand near chin, no cigarette), the other hand in
> his pocket, strong red rim light from the left, isolated on a transparent
> background, vertical 450×730 crop.

### I10 — footer second still / frame 2 → `footer 2nd image.jpg`

> **Prompt:** [YOUR FACE] A man in a black suit and sunglasses leaning casually
> against a vintage red Ferrari 308, ankle crossed, elbow on the roof. The
> background splits diagonally: warm cream white on the left, saturated red on
> the right; glossy red floor with soft reflections. Editorial fashion
> photograph, hard studio light, 16:9.

---

## 4. Tool suggestions

| Job | Good tools |
|---|---|
| Face-consistent video | Kling 2.1 (face ref), Veo 3.1 (first-frame + ref), Runway Gen-4 (References), Sora (character) |
| Face-consistent stills | Midjourney `--cref`, GPT-image edit / Nano Banana (face swap into the shipped frames) |
| Plain artwork / cards | Midjourney v7, GPT-image, Flux |

**Quickest win:** don't regenerate everything — run the face-swap on the *shipped*
frames (`public/fin/man.png`, `public/projects/person.png`,
`public/years/figure.png`, first frame of each video). The composition is
already perfect; only the face changes.
