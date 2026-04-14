# Carasoul template

Bloggo Instagram Carousel — Styling Blueprint

This is the single source of truth for all Bloggo carousel visual design.
Read this before building any carousel. Follow every rule.


Canvas Specs
PropertyValuePlatformInstagramAspect ratio4:5 portraitCanvas size1080 × 1350 pxPadding60px all sidesSafe zone top90px minimumSafe zone bottom110px minimumBackground#FFFFFF white — always, every slide

Color System
RoleValueUsageBackground#FFFFFFEvery slide, no exceptionsPrimary text#1A1A1AHeadlines, body copyAccent#138EFFLabels, logo, CTA text, accent bars, linksMuted text#6B7280Italic subtext, secondary linesMuted light#9CA3AFLowest-emphasis text
Gradient Text (Slide 2 only)
cssbackground: linear-gradient(135deg, #138EFF 0%, #3BBAFF 35%, #6DD5FA 65%, #59E0C5 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
Direction: 135° diagonal. Flows from Bloggo blue → cyan → soft teal.

Typography System
Two-Font Rule
FontWhereWeightChewySlide 1 (hook) and Slide 10 (CTA) onlyRegular (400)Glacial IndifferenceSlides 2–9 (all middle slides)Regular (400) for body, Bold (700) for keywords
Chewy (Slides 1 & 10)

Playful, rounded, high-energy display font
Never used on middle content slides
Size: 56–68px for main headlines, 44px for CTA body

Glacial Indifference (Slides 2–9)

Clean, modern, geometric sans-serif
Regular weight for body text
Bold weight for key emotional words — critical for scannability
Italic for reflective/emotional subtext lines
Size: 38–56px for headlines, 22px for labels

Bold Keyword Strategy
On every middle slide, bold the 1–3 words that carry the emotional weight. The reader's eye should catch the bolded words even on a fast scroll.
Rule: bold the phrase that would stop someone mid-scroll if it were the only thing they read.

Slide Architecture
Slide 1 — Hook (Chewy)

Full white background
Centered text, single headline
Chewy font, 68px
First line: #1A1A1A dark text
Second line: #138EFF accent blue
Subtle dot pattern background at 4% opacity (optional)
Mascot placeholder: bottom-left
No paw, no Bloggo logo

Slide 2 — Transition (Glacial Indifference)

Centered text, single line
Gradient text effect (blue → cyan → teal)
Glacial Indifference Bold, 54px
Key words additionally bolded for emphasis
Bloggo logo: bottom-left
Cat paw: bottom-right

Slides 3–8 — Content Slides (Glacial Indifference)

Left-aligned text — every content slide, no exceptions
Blue accent bar: 8px wide, left edge, 12% opacity
Subtle blue gradient zone on right side at 7% opacity
Label: Glacial Indifference Bold, 22px, #138EFF, uppercase, letter-spacing 2px
Body text: Glacial Indifference Regular, 40px, #1A1A1A
Italic subtext: Glacial Indifference Italic, #6B7280
Bold keywords within body text
Bloggo logo: bottom-left
Cat paw: bottom-right

Slide 9 — Insight / Save-Worthy (Glacial Indifference)

Centered text
Two-tier typography:

Top line: Glacial Indifference Regular, 38px, #6B7280 muted
Bottom line: Glacial Indifference Bold, 56px, #1A1A1A


Pure typography, no images — this is the save-bait slide
Mascot placeholder: bottom-right
Bloggo logo: bottom-left
Cat paw: bottom-right

Slide 10 — CTA (Chewy)

Centered layout
Logo row: Bloggo app icon (72px, 16px border-radius) + "Bloggo" in Chewy, 56px, #138EFF
CTA headline: Chewy, 44px, #1A1A1A
CTA accent line: Chewy, 44px, #138EFF
"Link in bio": Glacial Indifference Bold, 22px, #138EFF, uppercase, letter-spacing 3px
Mascot placeholder: bottom-left
No paw on this slide
No Bloggo text logo watermark (the logo row replaces it)


Recurring Elements
Bloggo Logo Watermark
PropertyValuePositionBottom-left, 60px from left edge, 40px from bottomFontChewySize28pxColor#138EFF at 60% opacityText"Bloggo" (capital B)Appears onSlides 2–9 only
Cat Paw Swipe Indicator
PropertyValuePositionBottom-right, 24px from right, 16px from bottomSize130px width, auto heightImageBlack cat paw pointing right (transparent PNG)Appears onSlides 2–9 onlyNot onSlide 1 and Slide 10
Bloggo App Icon (Slide 10 only)
PropertyValueSize72 × 72pxBorder radius16pxPositionLeft of "Bloggo" text in logo row, centeredGap18px between icon and text
Mascot Placeholder
PropertyValueSize150–160px squareBorder2.5px dashed, rgba(19,142,255,0.3)Border radius24px
Positions: Slide 1 bottom-left, Slide 9 bottom-right, Slide 10 bottom-left.

Layout Rules

All content slides (3–8) are left-aligned. Never center a content slide.
Slides 1, 2, 9, and 10 are center-aligned.
Every slide has one clear focal point — never overload.
Each slide must be readable in under 2 seconds.
Max 10 words per slide.
Use line breaks with 6px margin-top for breathing room between text lines.


Accent Bar
PropertyValueWidth8pxPositionLeft edge of slide, full heightColor#138EFF at 12% opacityAppears onLeft-aligned content slides (3, 4, 6, 7, 8)Not onCentered slides (1, 2, 5, 9, 10)

Background Textures
LocationTextureSlide 1Dot pattern — #138EFF dots, 4% opacity, 36px gridContent slidesRight-side gradient — rgba(19,142,255,0.04–0.06), 45% widthCentered content slideCentered radial gradient — rgba(19,142,255,0.05), 4% opacityAll othersClean white, no texture
These are extremely subtle. They add depth without competing with text.

Consistency Checklist
Before exporting any carousel, verify:

 Background is #FFFFFF on every slide
 Accent color is #138EFF everywhere
 Slide 1 uses Chewy font
 Slides 2–9 use Glacial Indifference
 Slide 10 uses Chewy font
 Bold keywords applied on slides 2–9
 All content slides (3–8) are left-aligned
 Cat paw appears bottom-right on slides 2–9 only
 Bloggo logo appears bottom-left on slides 2–9 only
 "Bloggo" is capitalized everywhere
 Slide 10 has app icon left of "Bloggo" title
 Slide 2 uses gradient text
 No slide exceeds 10 words
 Brand voice check passed (see bloggo-brand.md)
 No cloud features mentioned (V1 only)