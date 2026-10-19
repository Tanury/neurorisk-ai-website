"""Rebuilds every page of the R26-DS-015 site. Edit the CONTENT section, then run:  python3 build.py
The output is plain HTML + CSS (no JavaScript), ready to upload as-is."""
import html, os
E = html.escape
OUT = os.path.dirname(os.path.abspath(__file__))
SP = os.path.dirname(__file__)

NAME = "NeuroRisk AI"
CODE = "R26-DS-015"

# ---------------------------------------------------------------- icons
I = {
 "brain":'<path d="M9 3a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a2 2 0 0 0-3-2z"/><path d="M15 3a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/>',
 "eye":'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "wave":'<path d="M2 12h3l2-6 4 12 3-9 2 3h6"/>',
 "flask":'<path d="M9 3h6"/><path d="M10 3v6L4 19a1.5 1.5 0 0 0 1.3 2h13.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7 15h10"/>',
 "merge":'<circle cx="6" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="12" r="2"/><path d="M8 6c5 0 5 6 8 6M8 18c5 0 5-6 8-6"/>',
 "upload":'<path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/>',
 "sliders":'<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>',
 "cpu":'<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
 "chart":'<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
 "alert":'<path d="M12 3 2 20h20L12 3z"/><path d="M12 10v4M12 17h0"/>',
 "bulb":'<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z"/>',
 "book":'<path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4z"/><path d="M20 4h-6a3 3 0 0 0-3 3"/><path d="M20 4v14h-7"/>',
 "search":'<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
 "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "layers":'<path d="m12 3 9 5-9 5-9-5 9-5z"/><path d="m3 13 9 5 9-5"/>',
 "shield":'<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3z"/><path d="m9 12 2 2 4-4"/>',
 "monitor":'<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 "server":'<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h0M7 16.5h0"/>',
 "file":'<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
 "ext":'<path d="M14 4h6v6M20 4l-9 9"/><path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
 "play":'<circle cx="12" cy="12" r="9"/><path d="m10 8 6 4-6 4z"/>',
 "mail":'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "phone":'<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
 "pin":'<path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "in":'<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7h0M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
 "award":'<circle cx="12" cy="9" r="6"/><path d="m9 14.5-1.5 6.5L12 19l4.5 2-1.5-6.5"/>',
 "check":'<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
 "chev":'<path d="m6 9 6 6 6-6"/>',
 "flag":'<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
 "slides":'<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M12 16v4M8 20h8M10 8l4 2-4 2z"/>',
 "users":'<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.5A5 5 0 0 1 21 19"/>',
 "cog":'<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
}
def logo_file(name):
    for ext in ("svg", "png", "webp"):
        if name and os.path.exists(os.path.join(OUT, "images", "tech", f"{name}.{ext}")):
            return f"{name}.{ext}"
    return ""
def ic(n): return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{I.get(n, I["file"])}</svg>'
def ini(n):
    w = [x for x in n.replace(".", " ").split() if x[0].isalpha()]
    return "".join(x[0].upper() for x in w[:2])

# ================================================================ CONTENT
# Edit these lists, then run `python3 gen.py` to rebuild every page.
# Links: put files in documents/ or slides/ (relative paths), or paste a
# Google Drive "anyone with the link" URL. Leave "" while pending.

TITLE = "Multimodal AI for early risk assessment of neurodegenerative diseases"
HIGHLIGHT = "early risk assessment"
LEDE = ("Combining brain MRI, retinal OCT, EEG and fluid biomarkers to flag early signs of Alzheimer's, "
        "Parkinson's and multiple sclerosis, with an explanation for every prediction.")

ABSTRACT = [
 "Neurodegenerative diseases such as Alzheimer's disease (AD), Parkinson's disease (PD) and multiple sclerosis (MS) "
 "are usually diagnosed only after clear symptoms appear, when a large part of the damage cannot be reversed. "
 "Early signs exist in brain scans, retinal images, brain signals and blood or spinal fluid, but each test is "
 "read separately and none is reliable enough on its own.",
 "This project builds a multimodal system that brings these signals together. Each modality has its own encoder: "
 "a vision encoder for MRI, DaTscan SPECT and retinal OCT, an EEG encoder, a fluid biomarker model as well as a voice encoder. Every encoder produces an "
 "embedding in the same format, and an adaptive fusion engine combines whatever embeddings are available for a "
 "patient into a risk score for each disease. Grad-CAM heatmaps and feature-impact views show which inputs drove "
 "each result, and a web dashboard presents the scores to clinicians.",
]
KEYWORDS = ["Neurodegenerative disease", "Multimodal fusion", "Medical imaging", "Retinal OCT", "EEG",
            "Fluid Biomarkers", "Explainable AI"]

MODALITIES = [
 ("eye", "Vision (Imaging) Encoder", "MRI and retinal OCT turned into a shared image embedding"),
 ("wave", "EEG Encoder", "Brain signal patterns linked to early decline"),
 ("flask", "Fluid Biomarker Encoder", "Lab markers that change before symptoms appear"),
 ("merge", "Fusion Engine", "One risk score per disease, with the reasons behind it"),
]

FEATURES = [
 ("layers", "Multi-disease screening", "One pipeline assesses Alzheimer's, Parkinson's and multiple sclerosis."),
 ("shield", "Works with missing data", "Risk is still estimated when only some tests are available."),
 ("eye", "Retinal screening", "OCT layer thickness offers a cheaper, faster check alongside MRI."),
 ("brain", "Visual explanations", "Grad-CAM heatmaps highlight the brain regions behind a prediction."),
 ("merge", "Shared embedding format", "Every branch outputs the same 256-d vector, so new modalities plug in easily."),
 ("monitor", "Clinician dashboard", "Upload data, view scores and explanations in a single web app."),
]

USE_CASES = [
 ("search", "Early screening", "Flag patients for follow-up before clear symptoms appear."),
 ("monitor", "Clinical decision support", "Give neurologists a combined view of scans, signals and lab results."),
 ("eye", "Low-resource settings", "Use retinal OCT where MRI access is limited or expensive."),
 ("layers", "Research cohorts", "Compare risk across patients using a consistent embedding format."),
]

LITERATURE = [
  "Brain imaging research for AD, PD and MS still has clear limitations. Most deep learning models target a single "
 "disease and are trained on one public cohort such as ADNI, so they often generalise poorly to scans from other "
 "hospitals, scanners and acquisition protocols [2]. Labelled 3D scans are scarce, which is why many studies depend "
 "on residual networks and transfer learning from medical pre-training sets to limit overfitting [1], [3]. Early "
 "changes in PD are subtle on structural MRI, and MS models usually rely on lesion masks that vary between "
 "annotators and rarely include healthy controls. As a result, most imaging work detects established disease "
 "rather than early risk.",
 "Retinal OCT has emerged as a low-cost window into the central nervous system. Thinning of inner retinal layers "
 "is linked to multiple sclerosis and other neurodegenerative conditions, and public datasets with manual layer "
 "delineations now exist [4].",
 "For brain signals, compact deep learning models such as EEGNet allow efficient EEG analysis, but most studies "
 "focus on a single neurological disease [5]. Subject-level data leakage, where recordings from the same person "
 "appear in both training and test sets, can also inflate reported accuracy, which highlights the need for "
 "subject-independent evaluation [6].",
 "Fluid biomarkers such as neurofilament light chain (NfL) reflect neuronal damage, but a single marker can change "
 "across several neurological disorders. The literature therefore stresses combining biomarkers with clinical "
 "information to support disease assessment [7].",
 "Speech also carries measurable markers of neurological disease [8], yet it is rarely included in multimodal "
 "neurological risk models.",
 "Most published models still use a single modality and a single disease. Where multimodal work exists, it often "
 "assumes every input is present for every patient, which does not reflect clinical practice, although methods "
 "such as M3Care show that learning with missing modalities is possible [9].",
 "Explainability methods such as Grad-CAM make CNN predictions easier to check [10], and approaches such as SHAPE "
 "measure how much each modality contributes to a multimodal prediction [11]. Missing-modality learning, "
 "uncertainty quantification and explainability are each well developed, but they have largely been studied in "
 "isolation and are rarely brought together in one end-to-end diagnostic tool.",
]
GAPS = [
 "Few systems cover more than one neurodegenerative disease in one pipeline.",
 "Imaging, EEG and biomarker models are developed separately with no shared output format.",
 "Fusion methods rarely handle patients with missing modalities.",
 "Explanations are often missing or not shown in a form clinicians can use.",
]
PROBLEM = ("Neurodegenerative diseases are usually diagnosed after symptoms appear, when much of the damage is already "
 "done. Each test (a MRI scan, an OCT, an EEG, a blood panel) is read on its own, by a different specialist, and no single test "
 "is reliable enough for early detection. Useful signals are spread across modalities and rarely combined.")
RESEARCH_Q = "How can brain and retinal imaging, EEG and fluid biomarker data be combined into one explainable early-risk assessment for AD, PD and MS, even when some of these inputs are missing?"
SOLUTION = ("Each modality has its own encoder that produces a fixed-size embedding. An adaptive fusion engine combines "
 "whatever embeddings are available into a risk score for each disease, and Grad-CAM and feature-impact views show "
 "which regions and inputs drove each result.")

MAIN_OBJECTIVE = "Build an explainable multimodal system that estimates early risk of Alzheimer's Disease, Parkinson's Disease and Multiple Sclerosis from brain and retinal imaging, EEG, voice recordings and fluid biomarker data."
OBJECTIVES = [
 ("eye", "Vision (Imaging) Encoder", "Dissanayaka D. M. T. M", [
   "Build image encoders for brain MRI, DaTscan SPECT and retinal OCT that pair each disease with its most suitable modality",
   "Output a 256-dimensional L2-normalised embedding from every branch through a shared output head for multimodal integration",
   "Provide Grad-CAM maps and visual overlays so clinicians can see which regions of the scan drove each prediction"]),
 ("wave", "EEG Encoder", "Sudugodage S. R", [
   "Extract features from EEG recordings linked to early neurodegeneration",
   "Train an EEG encoder that outputs embeddings in the shared format",
   "Evaluate if the learned embeddings effectively capture patterns that help distinguish healthy controls from individuals with neurodegenerative conditions."]),
 ("flask", "Fluid Biomarker Encoder", "Danishiya Appulingam", [
   "Model fluid biomarker values associated with each disease",
   "Produce biomarker embeddings for the fusion engine",
   "Evaluate the effectiveness of the biomarker embeddings in capturing relevant information for early risk assessment."]),
 ("merge", "Fusion Engine", "Aarabhi A. Y", [
   "Combine available embeddings with an adaptive fusion method",
   "Output per-disease risk scores that work with missing inputs",
   "Show each modality’s probabilities, its weight and contribution, and an agreement label (Strong, Partial or Discordant), so a clinician can recompute the fused score."]),
]

PIPELINE = [
 ("upload", "Collect inputs", "Scans, EEG and lab results are uploaded for a patient."),
 ("sliders", "Preprocess", "Registration, skull stripping, signal cleaning and normalisation."),
 ("cpu", "Encode", "Each branch outputs a 256-d embedding in the same format."),
 ("chart", "Fuse and explain", "Risk scores per disease, with heatmaps and feature impact."),
]
METHODS = [
 ("eye", "Vision (Imaging) Encoder", "Dissanayaka D. M. T. M",
  "Five pathology-matched branches, one per disease and imaging type, sharing one output head that gives the same 256-d embedding.",
  ["AD: dual-stream 3D and 2D ResNet-18 on T1 MRI from ADNI (AD, MCI and CN)",
   "PD: 2D CNN on a specific-binding-ratio slice of DaTscan SPECT from PPMI, with a supplementary structural MRI branch",
   "MS (MRI): MindGlide segmentation, then five region volumes normalised by total brain volume (MS3SEG with LEMON controls)",
   "MS (OCT): multilayer perceptron on eight retinal layer thicknesses from the JHU OCT dataset",
   "Evaluation: held-out test sets for ADNI and PPMI; leave-one-out cross-validation for the small MS cohorts"]),
 ("wave", "EEG Encoder", "Sudugodage S. R",
  "Turns raw resting-state EEG into a 256-d embedding with separate AD, PD and MS risk scores.",
  ["Data: OpenNeuro AD/FTD/HC and UC San Diego PD resting-state EEG, giving a 115-subject reference cohort",
   "Preprocessing: common 19-channel montage, 0.5–40 Hz band-pass filter, automated FastICA artifact removal and 4-second epochs with amplitude rejection",
   "Model: hybrid STFT and Morlet wavelet time–frequency inputs to an encoder with a shared projection head and L2 normalisation",
   "Evaluation: subject-grouped five-fold cross-validation with an automated leakage check",
   "Returns a zero vector and an availability flag when EEG is missing or fails quality control"]),
 ("flask", "Fluid Biomarker Encoder", "Danishiya Appulingam",
  "Interprets fluid biomarkers together with demographic, clinical, functional and genetic information.",
  ["Data: combined 24-feature dataset of 10,000 records, split 7,000 / 1,500 / 1,500",
   "Features: eight fluid biomarkers (Aβ42/40, total tau, p-tau181, NfL, GFAP, α-synuclein, GDF15, CRP) with demographic, cognitive, sleep, motor, functional and genetic variables",
   "Preprocessing: median imputation with missingness indicators, standardisation and one-hot encoding in scikit-learn pipelines; values can be extracted from lab reports for user review",
   "Models: Extra Trees for the disease pattern (AD, Healthy, MS, PD) and Logistic Regression for the Low, Medium or High risk level, chosen by macro F1",
   "Evaluation: 96.33% pattern accuracy and 95.53% risk-level accuracy on 1,500 held-out records"]),
 ("merge", "Fusion Engine", "Aarabhi A. Y",
  "Combines the voice, biomedical and EEG outputs into one risk level per disease.",
  ["Fusion approach: quality-weighted late fusion; each modality's output becomes evidence for each disease, is weighted by input quality and averaged into a Low, Moderate or High risk level",
   "Missing modalities: poor-quality inputs get less weight and missing biomarker values are imputed and counted; the current version needs voice, biomedical and EEG for the same participant, and a masked-attention engine for any subset was designed but not built",
   "Explainability and evaluation: the dashboard shows each modality's probabilities, weight, contribution and an agreement label (Strong, Partial or Discordant); reviewed by the clinical supervisor, but not yet evaluated against outcomes because no dataset has more than one modality for the same people"]),
]
ARCH = ("The system has four layers. Inputs are processed by a separate encoder per modality, the fusion engine turns "
 "the combined embeddings into risk scores and explanations, and a FastAPI backend serves results to the dashboard.")

# (name, logo file name in images/tech/ without extension, letters shown when no logo file exists)
# To show a logo, save it as images/tech/<name>.svg or .png (e.g. images/tech/python.svg) and rebuild.
TECH = [("Python","python","Py"),("PyTorch","pytorch","PT"),("MONAI","monai","MO"),("scikit-learn","scikitlearn","SK"),
        ("NumPy","numpy","NP"),("Pandas","pandas","PD"),("FSL","fsl","FSL"),("ANTs","ants","ANT"),("NiBabel","nibabel","NB"),
        ("MindGlide","mindglide","MG"),("FastAPI","fastapi","API"),("Next.js","nextdotjs","NX"),("React","react","RE"),
        ("Google Colab","googlecolab","CO"),("Weights & Biases","weightsandbiases","WB"),("GitHub","github","GH")]

# status: done | now | upcoming
# (id, date or "" to hide, name, status, marks or "", description, what is assessed)
MILESTONES = [
 ("taf", "", "Topic Assessment Form (TAF)", "done", "",
  "Submission and presentation of the research topic, scope and team for approval.",
  ["Research topic and problem", "Scope and individual components", "Supervisor and co-supervisor approval"]),
 ("proposal", "", "Project Proposal (Presentation + Report)", "done", "",
  "Each member presents and submits a proposal for their component.",
  ["Literature review and research gap", "Objectives and methodology", "Planned timeline and resources"]),
 ("pp1", "", "Progress Presentation 1", "done", "",
  "First progress review, at roughly 50% of the work.",
  ["Literature survey", "Datasets and preprocessing", "Preliminary results"]),
 ("pp2", "", "Progress Presentation 2", "done", "",
  "Second progress review, at roughly 90% of the work.",
  ["Trained models and evaluation", "System integration", "Remaining work"]),
 ("draft-thesis", "", "Draft Thesis and Website Submission", "done", "",
  "Submission of the draft thesis for review, together with this project website.",
  ["Draft individual thesis", "Project website"]),
 ("logbook", "", "Logbook and Checklist Submissions", "now", "",
  "Research logbook and the submission checklists.",
  ["Logbook of research activities", "Checklist documents"]),
 ("final", "20 Oct 2026", "Final Presentation & Viva", "done", "",
  "Final demonstration of the complete system and oral defence.",
  ["Live demonstration", "Individual viva"]),
 ("website", "20 Oct 2026", "Website Assessment", "now", "",
  "Assessment of this project website.",
  ["Structure, content and navigation", "Documents and slides available"]),
 ("paper", "", "Research Paper Submission", "upcoming", "",
  "Submission of a research paper describing the system and findings.",
  ["Paper written to the conference format", "Methodology, results and discussion"]),
 ("final-thesis", "", "Final Thesis Submission", "upcoming", "",
  "Final individual thesis for each component and one group report for the full system.",
  ["Individual final thesis", "Group final report"]),
]

# (group, note, status: done | now | upcoming, [(document name, link)])
# Paste a Google Drive "anyone with the link" URL as the link; leave "" while pending.
DOCUMENTS = [
 ("Project Charter", "Approved topic, scope and team.", "done", [
   ("Project Charter (TAF)", "https://drive.google.com/file/d/1bESpBGm1lo70Q-X-Um_qroWM4TYzFNAp/view?usp=share_link")]),
 ("Proposal Documents", "Individual proposal reports for each member.", "done", [
   ("Proposal — Dissanayaka D. M. T. M", "https://drive.google.com/file/d/1svylC0e1Fyo0_bSDFtGGYAe2-xfRZFSq/view?usp=share_link"), ("Proposal — Sudugodage S. R", "https://drive.google.com/file/d/18vATlpxY6rkbAUlLGKr4nXmOQXY09wkl/view?usp=share_link"),
   ("Proposal — Aarabhi A. Y", "https://drive.google.com/file/d/1HBKPnstFyMppco2UJ128wkgF4RQCzlH_/view?usp=share_link"), ("Proposal — Danishiya Appulingam", "https://drive.google.com/file/d/1n02K_VRajzH4D7Lv92QjyDYjxuykh3jr/view?usp=share_link")]),
 ("Checklist Documents", "Supporting reports required for submission.", "done", [
   ("Literature review master sheet", "https://docs.google.com/spreadsheets/d/1lrwGDo5HV9n5vyC0cXNRqEz2mHR7DYSn/edit?usp=share_link&ouid=107658917753633491887&rtpof=true&sd=true"), ("Data analysis report", "https://drive.google.com/file/d/1uTq2UxEO21-CkjQDgqu0Q3HBdrw7yRno/view?usp=share_link"),
   ("Ethical analysis report", "https://drive.google.com/file/d/1BF0ZtpRR2ctGX94VJulj85yXp1v5OnM4/view?usp=share_link"), ("MLOps report", "https://drive.google.com/file/d/1hjIehHhOR1YNM5vQhKLqLHPEnuqr0qmI/view?usp=share_link")]),
 ("Draft Thesis", "Draft individual theses and the main group draft.", "done", [
   ("Draft Thesis — Group (main)", "https://drive.google.com/file/d/19H3kfNYYJTwZezm-t7Sfo0frOZsiw8iI/view?usp=share_link"), ("Draft Thesis — Dissanayaka D. M. T. M", "https://drive.google.com/file/d/1WOIVhubDdG_XY_at2QEFJFFkBM_Banc8/view?usp=share_link"),
   ("Draft Thesis — Sudugodage S. R", "https://drive.google.com/file/d/1swKZUoEJwO4t_6t4ieb_esqqdnuaBSIx/view?usp=share_link"), ("Draft Thesis — Aarabhi A. Y", "https://drive.google.com/file/d/14u03W9u6ADtDJ0JsMDN0JDIcLm9Q6csZ/view?usp=share_link"),
   ("Draft Thesis — Danishiya Appulingam", "https://drive.google.com/file/d/10LTtbo6BSo9sdQbYPz9T7SHa8x1NDILX/view?usp=share_link")]),
 ("Final Documents", "Individual final reports and the main group report.", "upcoming", [
   ("Final Report — Group (main)", ""), ("Final Report — Dissanayaka D. M. T. M", ""),
   ("Final Report — Sudugodage S. R", ""), ("Final Report — Aarabhi A. Y", ""),
   ("Final Report — Danishiya Appulingam", "")]),
 ("Research Paper", "Full paper with method, results and conclusions.", "upcoming", [
   ("Research Paper — Full Version", "")]),
]

PRESENTATIONS = [
 ("Proposal Presentation", "Problem, objectives and planned method for each component.", "done", "https://drive.google.com/file/d/1ppvsT6N100F5wnnnFg6BqZHqeKl1xhdt/view?usp=sharing"),
 ("Progress Presentation 1", "Literature review, datasets and first experiments.", "done", "https://drive.google.com/file/d/1sGRdBrWa60Z3i4eYzAbRxfxH50XBKADf/view?usp=share_link"),
 ("Progress Presentation 2", "Model results, evaluation and system integration.", "done", "https://drive.google.com/file/d/1lZee7vji6kFMrE0_WN9kgHvq5GBGM5sL/view?usp=share_link"),
 ("Final Presentation", "Complete system, findings and live demonstration.", "upcoming", ""),
]

# name, role pill, position, email, linkedin, photo
SUPERVISORS = [
 ("Dr. Lakmini Abeywardhana", "Supervisor",
  "Assistant Professor | Department of Computer Science | Faculty of Computing", "lakmini.d@sliit.lk", "", "images/team/drlakmini.jpeg"),
 ("Dr. Mahima Weerasinghe", "Co-supervisor", "Head of School of Business and AI", "mahima.w@sliit.lk", "", "images/team/drmahima.jpg"),
]
# name, student ID, component, email, linkedin, photo
TEAM = [
 ("Dissanayaka D. M. T. M", "IT22203762", "Vision (Imaging) Encoder", "it22203762@my.sliit.lk", "", "images/team/tanuri.jpeg"),
 ("Sudugodage S. R", "IT22557742", "EEG Encoder", "it22557742@my.sliit.lk", "", "images/team/sanali.jpeg"),
 ("Aarabhi A. Y", "IT22118868", "Fusion Engine", "it22118868@my.sliit.lk", "", "images/team/aarabhi.jpeg"),
 ("Danishiya Appulingam", "IT22645098", "Fluid Biomarker Encoder", "it22645098@my.sliit.lk", "", "images/team/danishiya.jpeg"),
]
DEGREE = "Bachelor of Science (Hons) in Information Technology, specialising in Data Science"
# (status, title, text, accepted?, [(label, value)])
# (status, title, text, accepted?, [(label, value)], link or "")
ACHIEVEMENTS = [
 ("Paper Submitted", "8th IEEE International Conference on Advancements in Computing (ICAC 2026)",
  "Research paper submitted on learning shared representations from fluid biomarkers for cross-disease neurological risk assessment.",
  False,
  [("Paper Title", "Learning Representations from Fluid Biomarkers for Cross-Disease Neurological Risk Assessment"),
   ("Conference", "ICAC 2026, Faculty of Computing, SLIIT"),
   ("Dates", "9 – 10 December 2026, hybrid"),
   ("Proceedings", "IEEE Xplore, indexed in Scopus")],
  "https://icac.lk"),
 ("Abstract Submitted", "AAIC Neuroscience Next 2027",
  "Abstract submitted to the Alzheimer's Association conference for students and early-career researchers in neuroscience.",
  False,
  [("Organiser", "Alzheimer's Association"),
   ("Format", "Poster presentation if accepted, hybrid"),
   ("Dates", "15 – 18 February 2027")],
  "https://www.alz.org/neurosciencenext/abstracts"),
]

CONTACT_EMAIL = "neuroriskairesearch@gmail.com"
CONTACT_PHONE = "+94 70 660 2028"
GITHUB = "https://github.com/Tanury/R26-DS-015"
LOCATION = "SLIIT Malabe Campus, New Kandy Road, Malabe"

# ================================================================ LAYOUT
STATUS = {"done": "Completed", "now": "Ongoing", "upcoming": "Upcoming"}
PAGES = [("index.html", "Home"), ("domain.html", "Domain"), ("milestones.html", "Milestones"),
         ("documents.html", "Documents"), ("presentations.html", "Presentations"),
         ("about.html", "About Us"), ("contact.html", "Contact Us")]

def nav(cur):
    items = []
    for f, label in PAGES:
        act = ' class="active" aria-current="page"' if f == cur else ""
        if f == "milestones.html":
            dd = "".join(f'<li><a href="milestones.html#{m[0]}">{E(m[2])}</a></li>' for m in MILESTONES)
            items.append(f'<li class="has-dd"><a href="{f}"{act} aria-haspopup="true">{label}<span class="caret">▾</span></a>'
                         f'<ul class="dropdown" aria-label="Milestones">{dd}</ul></li>')
        elif f == "domain.html":
            subs = [("literature", "Literature Survey"), ("gap", "Research Gap"), ("problem", "Research Problem"),
                    ("objectives", "Research Objectives"), ("methodology", "Methodology"), ("technologies", "Technologies Used")]
            dd = "".join(f'<li><a href="domain.html#{a}">{t}</a></li>' for a, t in subs)
            items.append(f'<li class="has-dd"><a href="{f}"{act} aria-haspopup="true">{label}<span class="caret">▾</span></a>'
                         f'<ul class="dropdown" aria-label="Domain">{dd}</ul></li>')
        else:
            items.append(f'<li><a href="{f}"{act}>{label}</a></li>')
    return f'''<header class="nav"><div class="bar">
  <a class="logo" href="index.html"><span class="logo-badge">{ic("brain")}</span><span>{NAME}</span></a>
  <input type="checkbox" id="navToggle" aria-label="Toggle menu"><label for="navToggle" class="menu-btn">Menu</label>
  <ul id="navList">{"".join(items)}</ul>
</div></header>'''

def page(fname, title, desc, body, hero=True, crumb=None, show_desc=True, script=""):
    banner = ""
    if crumb:
        banner = f'''<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / {E(crumb)}</div>
  <h1>{E(crumb)}</h1>{f"<p>{E(desc)}</p>" if show_desc else ""}</div></section>'''
    foot = "".join(f'<a href="{f}">{l}</a>' for f, l in PAGES)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{E(desc)}">
<title>{E(title)} | {NAME} — {CODE}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{nav(fname)}
<main>
{banner}
{body}
</main>
<footer><div class="wrap"><span>© 2026 <b>{NAME}</b> Research Project. All rights reserved.</span><nav>{foot}</nav></div></footer>
{script}
</body>
</html>
'''

def sec(id_, title, sub, inner, cls=""):
    idattr = f' id="{id_}"' if id_ else ""
    return f'''<section class="sec {cls}"{idattr}><div class="wrap">
<div class="sec-head"><h2>{title}</h2><p>{E(sub)}</p></div>
{inner}
</div></section>'''

def link_btn(href, cls, label, icon):
    if href:
        tgt = ' target="_blank" rel="noopener"' if href.startswith("http") or href.endswith(".pdf") else ""
        return f'<a class="{cls}" href="{E(href)}"{tgt}>{ic(icon)}{label}</a>'
    return f'<span class="{cls}" aria-disabled="true">Coming soon</span>'

# ---------------------------------------------------------------- HOME
t = E(TITLE)
t = t.replace(HIGHLIGHT, f'<span class="hl">{HIGHLIGHT}</span>', 1)
hero_cards = "".join(f'<div class="hero-card"><div class="ic">{ic(i)}</div><h3>{E(n)}</h3><p>{E(d)}</p></div>' for i, n, d in MODALITIES)
home = f'''<section class="hero" id="home"><div class="wrap">
  <span class="pill">{CODE} Research Project Website</span>
  <h1>{t}</h1>
  <p class="lede">{E(LEDE)}</p>
  <div class="hero-actions"><a class="btn btn-cyan" href="domain.html">Explore Research</a><a class="btn btn-outline" href="documents.html">View Documents</a></div>
  <div class="hero-cards">{hero_cards}</div>
</div></section>
''' + sec("abstract", "Abstract", "A short summary of the research.",
  f'<div class="card abstract">{"".join(f"<p>{E(p)}</p>" for p in ABSTRACT)}'
  f'<div class="kw">{"".join(f"<span>{E(k)}</span>" for k in KEYWORDS)}</div></div>') \
  + sec("", "Core Features", "What the system offers clinicians and researchers.",
  '<div class="grid2">' + "".join(f'<div class="card feat"><div class="icon-box">{ic(i)}</div><div><h4>{E(n)}</h4><p>{E(d)}</p></div></div>' for i, n, d in FEATURES) + '</div>', "soft")

use_cases = sec("use-cases", "Use Cases", "Where multimodal risk assessment can help.",
  '<div class="grid4">' + "".join(f'<div class="card uc"><div class="icon-box" style="margin-bottom:12px">{ic(i)}</div><h4>{E(n)}</h4><p>{E(d)}</p></div>' for i, n, d in USE_CASES) + '</div>')
#+ sec("", "Core Features", "What the system offers clinicians and researchers.",
  #'<div class="grid2">' + "".join(f'<div class="card feat"><div class="icon-box">{ic(i)}</div><div><h4>{E(n)}</h4><p>{E(d)}</p></div></div>' for i, n, d in FEATURES) + '</div>', "soft") \
#+ sec("", "Use Cases", "Where multimodal risk assessment can help.",
 # '<div class="grid4">' + "".join(f'<div class="card uc"><div class="icon-box" style="margin-bottom:12px">{ic(i)}</div><h4>{E(n)}</h4><p>{E(d)}</p></div>' for i, n, d in USE_CASES) + '</div>')

# ---------------------------------------------------------------- DOMAIN
subnav = '<nav class="subnav" aria-label="Domain sections"><div class="wrap">' + "".join(
  f'<a href="#{a}">{t}</a>' for a, t in [("literature", "Literature Survey"), ("gap", "Research Gap"),
   ("problem", "Research Problem"), ("objectives", "Research Objectives"), ("methodology", "Methodology"),
   ("technologies", "Technologies Used")]) + '</div></nav>'
refs = [
 "K. He, X. Zhang, S. Ren, and J. Sun, \"Deep residual learning for image recognition,\" in Proc. IEEE CVPR, 2016.",
 "C. R. Jack Jr. et al., \"The Alzheimer's Disease Neuroimaging Initiative (ADNI): MRI methods,\" J. Magn. Reson. Imaging, 2008.",
 "S. Chen, K. Ma, and Y. Zheng, \"Med3D: Transfer learning for 3D medical image analysis,\" arXiv:1904.00625, 2019.",
 "Y. He et al., \"Retinal layer parcellation of optical coherence tomography images: Data resource for multiple sclerosis and healthy controls,\" Data in Brief, 2019.",
 "V. J. Lawhern et al., \"EEGNet: A compact convolutional neural network for EEG-based brain–computer interfaces,\" Journal of Neural Engineering, 2018.",
 "G. Brookshire et al., \"Data leakage in deep learning studies of translational EEG,\" Frontiers in Neuroscience, 2024.",
 "M. Khalil et al., \"Neurofilaments as biomarkers in neurological disorders—towards clinical application,\" Nature Reviews Neurology, vol. 20, pp. 269–287, 2024. doi: 10.1038/s41582-024-00955-x.",
 "K. C. Fraser, J. A. Meltzer, and F. Rudzicz, \"Linguistic features identify Alzheimer's disease in narrative speech,\" Journal of Alzheimer's Disease, vol. 49, no. 2, pp. 407–422, 2016.",
 "C. Zhang, X. Chu, L. Ma, Y. Zhu, Y. Wang, J. Wang, and J. Zhao, \"M3Care: Learning with missing modalities in multimodal healthcare data,\" in Proc. 28th ACM SIGKDD Conf. Knowledge Discovery and Data Mining, 2022, pp. 2418–2428.",
 "R. R. Selvaraju et al., \"Grad-CAM: Visual explanations from deep networks via gradient-based localization,\" in Proc. IEEE ICCV, 2017.",
 "P. Hu, X. Li, and Y. Zhou, \"SHAPE: An unified approach to evaluate the contribution and cooperation of individual modalities,\" in Proc. 31st Int. Joint Conf. Artificial Intelligence (IJCAI), 2022, pp. 3064–3070.",
]
arch_nodes = [("brain", "Imaging Input", "MRI and retinal OCT"), ("monitor", "Clinician Dashboard", "Scores and explanations"),
              ("wave", "EEG + Biomarkers", "Signals and lab values"), ("server", "FastAPI + Storage", "Model services, .npz embeddings")]
node = lambda n: f'<div class="node"><div class="icon-box">{ic(n[0])}</div><strong>{E(n[1])}</strong><span>{E(n[2])}</span></div>'
arch = (f'<div class="arch-grid">{node(arch_nodes[0])}<div class="engine"><div class="icon-box">{ic("cpu")}</div>'
        f'<h5>Adaptive Fusion Engine</h5><p>Combines modality embeddings into per-disease risk scores</p></div>'
        f'{node(arch_nodes[1])}{node(arch_nodes[2])}{node(arch_nodes[3])}</div><p class="arch-text">{E(ARCH)}</p>')
domain_body = sec("literature", "Literature Survey", "What existing research has done.",
  f'<div class="card block-card"><div class="bh"><div class="icon-box">{ic("book")}</div><h3>Literature Survey</h3></div>'
  + "".join(f"<p>{E(p)}</p>" for p in LITERATURE) + '</div>'
  '<div class="refs"><h4>References</h4>' + "".join(f"<p>[{i+1}] {E(r)}</p>" for i, r in enumerate(refs)) + '</div>') \
+ sec("gap", "Research Gap", "What is still missing in existing work.",
  f'<div class="card block-card"><div class="bh"><div class="icon-box">{ic("search")}</div><h3>Research Gap</h3></div>'
  '<p>Despite recent progress, existing work still has clear limitations:</p><ul>'
  + "".join(f"<li>{E(g)}</li>" for g in GAPS) +
  '</ul><p>These gaps point to the need for one system that combines modalities, covers several diseases and explains its results.</p></div>', "soft") \
+ sec("problem", "Research Problem", "The problem this research addresses.",
  f'<div class="card ps"><div class="txt"><div><div class="icon-box">{ic("alert")}</div><h3>The Problem</h3><p>{E(PROBLEM)}</p></div>'
  f'<div><div class="icon-box">{ic("bulb")}</div><h3>Our Approach</h3><p>{E(SOLUTION)}</p></div></div>'
  f'<div class="card block-card" style="box-shadow:none;margin:0"><div class="bh"><div class="icon-box">{ic("search")}</div><h3>Research Question</h3></div><p>{E(RESEARCH_Q)}</p></div></div>') \
+ sec("objectives", "Research Objectives", "The main objective and each member's specific objectives.",
  f'<div class="card block-card"><div class="bh"><div class="icon-box">{ic("target")}</div><h3>Main Objective</h3></div><p>{E(MAIN_OBJECTIVE)}</p></div>'
  '<div class="grid2">' + "".join(
    f'<div class="card feat"><div class="icon-box">{ic(i)}</div><div><span class="who">{E(w)}</span><h4>{E(n)}</h4>'
    f'<ul>{"".join(f"<li>{E(x)}</li>" for x in items)}</ul></div></div>' for i, n, w, items in OBJECTIVES) + '</div>', "soft") \
+ sec("methodology", "Methodology", "How the system is built, from overall pipeline to each component.",
  '<div class="grid4">' + "".join(f'<div class="card step"><div class="icon-box">{ic(i)}</div><h4>{E(n)}</h4><p>{E(d)}</p></div>' for i, n, d in PIPELINE) + '</div>'
  f'<h3 class="people-title" style="margin-top:48px">System Architecture</h3><div class="card arch">{arch}</div>'
  '<h3 class="people-title" style="margin-top:48px">Component Methods</h3><div class="method">' + "".join(
    f'<div class="card"><h4><span class="icon-box" style="width:36px;height:36px">{ic(i)}</span>{E(n)} <span class="who">{E(w)}</span></h4>'
    f'<p>{E(d)}</p><ul>{"".join(f"<li>{E(x)}</li>" for x in items)}</ul></div>' for i, n, w, d, items in METHODS) + '</div>') \
+ sec("technologies", "Technologies Used", "The frameworks and tools behind each part of the system.",
  '<div class="tech">' + "".join((f'<div class="tech-item"><div class="tech-tile"><img src="images/tech/{logo_file(lg)}" alt="" width="38" height="38"></div><span>{E(n)}</span></div>' if logo_file(lg) else
   f'<div class="tech-item"><div class="tech-tile"><span class="fb">{E(a)}</span></div><span>{E(n)}</span></div>') for n, lg, a in TECH) + '</div>', "dark")

domain = subnav + domain_body

# ---------------------------------------------------------------- MILESTONES
ms = '<div class="ms-list">' + "".join(
 f'''<details class="ms" id="{mid}"{" open" if st == "now" else ""}>
  <summary><h3>{E(name)}{f' <span class="date">{E(when)}</span>' if when else ""}</h3><span class="status {st}">{STATUS[st]}</span><span class="chev">{ic("chev")}</span></summary>
  <div class="ms-body"><p>{E(d)}</p><strong style="color:var(--ink)">What is assessed</strong>
  <ul>{"".join(f"<li>{E(x)}</li>" for x in items)}</ul>
  {('<div class="row">' + (f'<span class="marks">Date: {E(when)}</span>' if when else '') + (f'<span class="marks">Marks: {E(marks)}</span>' if marks else '') + '</div>') if (when or marks) else ''}</div>
</details>''' for mid, when, name, st, marks, d, items in MILESTONES) + '</div>'
timeline = '<ol class="tl">' + "".join(
  f'<li><a class="card tl-card" href="#{mid}"><div class="meta"><span class="date">{E(w)}</span>'
  f'<span class="status {st}">{STATUS[st]}</span></div><h4>{E(n)}</h4></a></li>'
  for mid, w, n, st, _, _, _ in MILESTONES) + '</ol>'
milestones = sec("", "Assessments", "Select an assessment to see its details.", ms) \
  + sec("", "Timeline", "Every assessment in order, with its current status.", timeline, "soft")

# ---------------------------------------------------------------- DOCUMENTS
docs = '<div class="docs">' + "".join(
  f'''<div class="doc-card"><span class="avail {st}">{STATUS[st]}</span>
  <h3>{E(g)}</h3><p>{E(note)}</p>''' + "".join(
   f'<div class="doc-row"><span class="fi">{ic("file")}</span><div class="dm"><strong title="{E(n)}">{E(n)}</strong>'
   f'<span>{"PDF Document" if f else "Link coming soon"}</span></div>{link_btn(f, "view", "View", "ext")}</div>' for n, f in items) + '</div>'
  for g, note, st, items in DOCUMENTS) + '</div>'
documents = sec("", "Project Documents", "Documents already produced are linked for viewing; pending ones will be added when submitted.", docs, "soft")

# ---------------------------------------------------------------- PRESENTATIONS
pres = '<div class="grid2">' + "".join(
 f'<div class="card pres"><span class="status {s}">{STATUS[s]}</span><h4>{E(n)}</h4><p>{E(d)}</p>{link_btn(f, "btn-navy", "View Slides", "play")}</div>'
 for n, d, s, f in PRESENTATIONS) + '</div>'
presentations = sec("", "Research Presentations", "Slides from all reviews held throughout the research timeline", pres)

# ---------------------------------------------------------------- ABOUT
def person(name, pill, sub, comp, email, li, photo, sid=""):
    img = f'<img src="{E(photo)}" alt="{E(name)}">' if photo else ""
    soc = (f'<a href="mailto:{E(email)}" aria-label="Email {E(name)}" title="{E(email)}">{ic("mail")}</a>' if email else "") + \
          (f'<a href="{E(li)}" target="_blank" rel="noopener" aria-label="{E(name)} on LinkedIn">{ic("in")}</a>' if li else "")
    return (f'<div class="card person"><div class="avatar"><span>{ini(name)}</span>{img}</div><h4>{E(name)}</h4>'
            f'<span class="role-pill">{E(pill)}</span>' + (f'<div class="sid">{E(sid)}</div>' if sid else "") + f'<p>{E(sub)}</p>' + (f'<div class="comp">{E(comp)}</div>' if comp else "")
            + (f'<div class="socials">{soc}</div>' if soc else "") + '</div>')
ach = ("".join(
  f'<div class="card rc"><span class="status {"done" if acc else "now"}">{ic("check" if acc else "award")}{E(st)}</span>'
  f'<h3>{E(t)}</h3><p>{E(tx)}</p><div class="rc-grid">{"".join(f"<div{chr(32)+chr(99)+chr(108)+chr(97)+chr(115)+chr(115)+chr(61)+chr(34)+chr(119)+chr(105)+chr(100)+chr(101)+chr(34) if chr(84)+chr(105)+chr(116)+chr(108)+chr(101) in k else chr(32)[:0]}><small>{E(k)}</small><b>{E(v)}</b></div>" for k, v in det)}</div>'
  + (f'<a class="btn-navy" href="{E(link)}" target="_blank" rel="noopener" style="display:inline-flex;padding:10px 18px;margin-top:18px">{ic("ext")}Visit conference site</a>' if link else "") + '</div>'
  for st, t, tx, acc, det, link in ACHIEVEMENTS) if ACHIEVEMENTS else
  f'<div class="card empty">{ic("award")}<p style="margin-top:8px">Publications and awards will appear here once submitted.</p></div>')
about_people = sec("", "Project Supervisors", "The academic staff guiding the research.",
  '<div class="people sup">' + "".join(person(n, r, d, "", e, l, p) for n, r, d, e, l, p in SUPERVISORS) + '</div>') \
+ sec("", "Research Team", "Group members, their components and contact details.",
  '<div class="people team">' + "".join(person(n, "Undergraduate", DEGREE, c, e, l, p, sid) for n, sid, c, e, l, p in TEAM) + '</div>', "soft")
recognitions = sec("achievements", "Achievements &amp; Publications", "Papers, conferences and competitions connected to this research.",
  f'<div class="recog">{ach}</div>', "soft")
about = about_people + recognitions

# ---------------------------------------------------------------- CONTACT
#contact = sec("contact", "Contact Us", "Reach the team about the research, data or collaboration.",
# f'''<div class="contact cc-dark two">
#  <div class="cc"><div class="ci">{ic("mail")}</div><h4>Email Us</h4><p>Research questions and collaboration</p><a href="mailto:{E(CONTACT_EMAIL)}">{E(CONTACT_EMAIL)}</a></div>
#  <div class="cc"><div class="ci">{ic("pin")}</div><h4>Location</h4><p>Where the team is based</p><b>{E(LOCATION)}</b></div>
# </div>''', "dark first")

# CONTACT
import urllib.parse as up
EMAIL_SUBJECT = f"[{CODE}] Enquiry about the NeuroRisk AI research project"
EMAIL_BODY = ("Dear NeuroRisk AI Research Team,\n\n"
 "My name is [your name] from [organisation / institution].\n\n"
 "I am contacting you regarding [research collaboration / datasets / project details / other].\n\n"
 "[Write your message here.]\n\n"
 "Best regards,\n[your name]\n[contact number]")
mailto = f"mailto:{CONTACT_EMAIL}?subject={up.quote(EMAIL_SUBJECT)}&body={up.quote(EMAIL_BODY)}"
contact = sec("contact", "Contact Us", "Reach the team about the research, data or collaboration.",
  f'''<div class="contact cc-dark">
  <div class="cc"><div class="ci">{ic("mail")}</div><h4>Email Us</h4><p>Research questions and collaboration</p><a href="mailto:{E(CONTACT_EMAIL)}">{E(CONTACT_EMAIL)}</a></div>
  <div class="cc"><div class="ci">{ic("phone")}</div><h4>Phone</h4><p>Research team contact line</p><a href="tel:{E(CONTACT_PHONE.replace(" ", ""))}">{E(CONTACT_PHONE)}</a></div>
  <div class="cc"><div class="ci">{ic("pin")}</div><h4>Location</h4><p>Where the team is based</p><b>{E(LOCATION)}</b></div>
 </div>''', "dark first") \
+ sec("template", "Email Us", "Use this template so your message reaches the team with the details we need to respond quickly.",
 f'''<div class="card tpl" style="margin-top:0">
  <h3>Email template for inquiries related to NeuroRisk AI research project</h3><p>Subject: <b>{E(EMAIL_SUBJECT)}</b></p>
  <pre>{E(EMAIL_BODY)}</pre>
  <a class="btn-navy" href="{E(mailto)}">{ic("mail")}Open this template in your email app</a>
 </div>''', "soft")

# ---------------------------------------------------------------- WRITE
os.makedirs(f"{OUT}/css", exist_ok=True)
for d in ("documents", "slides", "images"):
    os.makedirs(f"{OUT}/{d}", exist_ok=True)
    open(f"{OUT}/{d}/.keep", "w").close()
# css/style.css is edited directly; this script only rebuilds the HTML pages.
# Home page scrolls through every section, first to last.
#home_full = (home + domain_body + milestones.replace('id="', 'id="home-ms-').replace('href="#', 'href="#home-ms-')
             #+ documents + presentations + use_cases + recognitions + about_people + contact.replace(' first"', '"'))
def part(nav_page, html_):
    return f'<div data-nav="{nav_page}">{html_}</div>'
home_full = (part("index.html", home)
             + part("domain.html", domain_body)
             + part("milestones.html", milestones.replace('id="', 'id="home-ms-').replace('href="#', 'href="#home-ms-'))
             + part("documents.html", documents)
             + part("presentations.html", presentations + use_cases)
             + part("about.html", recognitions + about_people)
             + part("contact.html", contact.replace(' first"', '"')))
SCROLL_SPY = """<script>
(function () {
  var parts = [].slice.call(document.querySelectorAll('[data-nav]'));
  var links = [].slice.call(document.querySelectorAll('#navList > li > a'));
  function update() {
    var cur = parts[0].getAttribute('data-nav');
    parts.forEach(function (p) { if (p.getBoundingClientRect().top < 140) cur = p.getAttribute('data-nav'); });
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4)
      cur = parts[parts.length - 1].getAttribute('data-nav');
    links.forEach(function (a) {
      var on = a.getAttribute('href') === cur;
      a.classList.toggle('active', on);
      if (on) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current');
    });
  }
  window.addEventListener('scroll', update, { passive: true });
  update();
})();
</script>"""
out = {
 "index.html": page("index.html", "Home", "Multimodal AI for early risk assessment of neurodegenerative diseases — R26-DS-015 research project.", home_full, script=SCROLL_SPY),
 "domain.html": page("domain.html", "Domain", "Literature survey, research gap, research problem, objectives, methodology and technologies.", domain, crumb="Domain"),
 "milestones.html": page("milestones.html", "Milestones", "Every assessment in the project, with its details, date and marks.", milestones, crumb="Milestones", show_desc=False),
 "documents.html": page("documents.html", "Documents", "Project charter, proposal, checklist and final documents.", documents, crumb="Documents"),
 "presentations.html": page("presentations.html", "Presentations", "Slides used in past presentations, with space for upcoming ones.", presentations, crumb="Presentations"),
 "about.html": page("about.html", "About Us", "Supervisors, group members, contact details and achievements.", about, crumb="About Us"),
 "contact.html": page("contact.html", "Contact Us", "Email and location for the research team.", contact),
}
for f, h in out.items():
    open(f"{OUT}/{f}", "w").write(h)
print("built", list(out))
