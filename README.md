# YOLO Ultralytics Computer Vision Examples

A set of standalone Python examples for trying common computer vision tasks with [Ultralytics YOLO](https://github.com/ultralytics/ultralytics). The repository includes scripts for object detection, segmentation, tracking, counting, pose estimation, customer detection, basic YOLO usage, and a YOLOv8n/OpenCV example.

> **Project status:** This repository is an example collection, not a packaged application. Each script is launched separately and may have its own image, video, camera, or model path configured in its source. Review the selected script and adjust those values for your machine before running it.

## Contents

| File | What it covers |
|---|---|
| `yolo_basics.py` | Introductory Ultralytics YOLO usage |
| `yolo_check.py` | YOLO setup or model check example |
| `object_detection.py` | Object detection |
| `object_segmentation.py` | Instance segmentation |
| `object_tracking.py` | Tracking detected objects across video frames |
| `object_counting.py` | Counting objects in a video or camera stream |
| `pose_estimation.py` | Human pose/keypoint estimation |
| `customer_detection.py` | Customer detection example |
| `yolov8_n_opencv.py` | YOLOv8n inference with OpenCV |
| `coco.txt` | COCO class-name list used by an example |

## Requirements

- Python 3.8 or later (use a version supported by your installed Ultralytics release)
- [Ultralytics](https://pypi.org/project/ultralytics/)
- OpenCV for scripts that read or display video (`opencv-python`)
- A webcam or local media file for scripts configured for live/video input
- Internet access on first run if the selected pretrained model weights are not already present

The repository does not include a dependency lock file. The commands below install the common packages used by this collection; individual scripts may require additional packages depending on their imports.

## Setup

Clone the repository and enter its directory:

```bash
git clone https://github.com/dhilleswar07/Yolo-Ultralytics.git
cd Yolo-Ultralytics
```

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the common dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install ultralytics opencv-python
```

If a script imports a package that is not installed, install that package in the same environment. For GPU use, install the PyTorch build compatible with the machine's CUDA setup by following the [PyTorch installation selector](https://pytorch.org/get-started/locally/), then install Ultralytics.

## Running the examples

Run a script from the repository root, for example:

```bash
python yolo_basics.py
```

To launch another example, replace the filename:

```bash
python object_detection.py
python object_segmentation.py
python object_tracking.py
python object_counting.py
python pose_estimation.py
python customer_detection.py
python yolov8_n_opencv.py
```

These are candidate entry points based on the repository's filenames; the exact command-line options, default input, display behavior, and output location depend on each script. Check the top of the script for its model and source settings. If the source is a webcam index, try `0` for the default camera. If it is a file path, use a path to an existing image or video and keep Windows path escaping in mind (for example, `r"C:\data\clip.mp4"` in Python).

### Typical Ultralytics workflow

The examples use the Ultralytics YOLO ecosystem. A basic Python prediction generally follows this pattern:

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("path/to/image.jpg")
```

This illustrates the general API; use the model names and calling pattern actually present in a particular repository script. Ultralytics can download supported pretrained weights when first requested. For webcam or video inference, the script may use a source such as `0` or a video filename and may display frames in an OpenCV window.

## Inputs, models, and outputs

- **Input source:** Depending on the example, this may be an image, a video file, or a camera stream. Set it in the script if no command-line argument is provided.
- **Model weights:** The script may refer to a pretrained `.pt` file or custom weights. Ensure the file exists, or allow Ultralytics to download a supported pretrained model.
- **Class names:** `coco.txt` is present for an example that needs a class-name list. Keep it in the expected location relative to that script, or update the path in the code.
- **Results:** Some scripts may display annotated frames, save output media, or only print detections. Check the script for its output settings and destination.

## COCO classes

COCO is a common object-detection dataset with predefined categories. The included `coco.txt` is a plain text class-name file. If a script reads it, its line order must match the class IDs produced by the model. Do not reorder or edit names unless you also update the class-ID mapping accordingly.

## Troubleshooting

- **`ModuleNotFoundError`:** Activate the virtual environment and install the missing package with `python -m pip install <package>`.
- **Model or weights file not found:** Check the model path in the script. Confirm the filename and working directory, or use a supported pretrained model name that Ultralytics can retrieve.
- **Image/video not found:** Check the configured source path. Relative paths are resolved from the current working directory, typically the repository root when following the commands above.
- **Camera does not open:** Close other camera applications, check OS camera permissions, and try a different camera index such as `0` or `1`.
- **OpenCV window is blank or closes immediately:** Confirm that the selected input is valid and that the script waits for a key press or loops over frames as intended. Headless environments may not support OpenCV display windows.
- **Slow inference:** Try a smaller model such as a nano variant, reduce image size if the script exposes that setting, or use compatible GPU-enabled PyTorch.
- **CUDA errors:** Verify that PyTorch detects the installed GPU and that the PyTorch/CUDA versions match. CPU inference can be used when no supported GPU setup is available.

## Limitations

This repository does not currently document a unified configuration format, command-line interface, automated test suite, or pinned dependency versions. As a result, examples may need small local changes for file paths, cameras, model weights, or the installed Ultralytics version. The README describes the files visible in the repository and does not claim that every script has been run or validated in every environment.

## License

No license file is listed in the repository. Unless the repository owner adds explicit licensing terms, ask the owner before reusing or redistributing this project's code. Ultralytics and its pretrained weights have their own licensing terms; review the [Ultralytics license information](https://www.ultralytics.com/license) separately for your intended use.

## References

- [Ultralytics documentation](https://docs.ultralytics.com/)
- [Ultralytics installation guide](https://docs.ultralytics.com/quickstart/)
- [Repository](https://github.com/dhilleswar07/Yolo-Ultralytics)
