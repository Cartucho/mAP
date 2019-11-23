import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mAP",
    version="0.0.1",
    author="Peter Siemen",
    author_email="mail@petersiemen.net",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/petersiemen/ya-yolo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        # TODO fix required depependency section in order to use ya-yolo as pip dependency in your project
        # 'torch==1.3.1',
        # 'torchvision==0.4.2',
        # 'numpy==1.17.4',
        # 'pillow = "*"
        # 'tqdm = "*"
        # 'onnx-coreml = "*"
        #onnx-coreml = {git = 'https://github.com/onnx/onnx-coreml.git', ref ='master', editable= true}
        #onnxmltools = "*"
        # onnxmltools = {git = 'https://github.com/onnx/onnx-coreml.git', ref = 'master',editable = true}
        # netron = "*"
        # coremltools = "*"
        #coremltools = {git= 'https://github.com/apple/coremltools.git', ref = 'master', editable = true}
        # nltk = "*"
        # cython = "*"
        # pycocotools = "*"'
        # 'mysql-connector-python==8.0.15',
        # 'PyMySQL==0.9.3'
    ]
)
