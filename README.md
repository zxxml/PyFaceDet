# PyFaceDet
PyFaceDet is a Python wrapper of libfacedetection. PyFaceDet 是 libfacedetection 人性化的 Python 封装。

## 中文文档

### 作用

PyFaceDet 旨在提供跨平台的开箱即用的人脸检测 API。

### 优点

- 跨平台（已在 Windows 10 x86_64 和 Ubuntu 18.04 x86_64 测试通过）
- 开箱即用（提供单一的 API，它可以接收不同类型的输入，并且返回统一的结果）
- 依赖项少（使用 `ctypes` 封装，只因功能需求引入 `pillow` 和 `numpy` 两个外部依赖）
- 性能损耗少（一定程度上优化了对 Python 数据结构的处理，还将继续进行优化）

### 使用方式

<del>将本项目存放到你喜欢的位置，然后想办法引用其中的 `facedetectcnn.py` 文件，该文件提供的 API 如下所示。</del>

使用 `pip install PyFaceDet` 安装它，然后在你的 Python 代码中导入它。顶层文件提供的 API 如下所示。

```python
facedetect_cnn(image: Union[str, Path, Image, np.ndarray, bytes], width: int = 0, height: int = 0, step: int = 0) -> Faces
```

你可以根据自己的需要传入图像路径（以字符串或 `Path` 对象的形式）、`PIL Image` 对象、BGR 格式的 `numpy` 数组或 `bytes` 对象。

当你传入 `PIL Image` 对象时，你可以选择同时提供 `width` 和 `height` 参数以修改传入 libfacedetection 的图像尺寸（请注意这还将**影响所得的结果**）。

当你传入 `bytes` 对象时，你必须同时提供 `width`、`height` 和 `step` 参数，它们分别代表图像的宽度、高度和每行字节数（通常为宽度的 3 倍）。

返回的 `Faces` 类型实际上是 `List[Tuple[int, int, int, int, int, int]]` 类型，六个整数分别为横坐标、纵坐标、长度、宽度、置信度、角度。

如果你正在使用如 PyCharm 等 IDE，你可能后发现顶层文件还提供其他两个 API。目前来说，它们仅仅是上述 API 的别名，你可以根据自己的喜好使用它们。

### 开发计划

- [ ] 开箱即用的多线程支持
- [ ] 树莓派支持（Raspbian）
- [ ] 更多的 Linux 发行版测试

## English

TODO