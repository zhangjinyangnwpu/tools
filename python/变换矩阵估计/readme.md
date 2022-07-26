### skimage.transform.estimate_transform

skimage 提供了一系列变化估计的方法，参考：https://scikit-image.org/docs/dev/api/skimage.transform.html#skimage.transform.estimate_transform

给定两组点，src 和 dst，得到对用的变化矩阵

```
import skimage

skimage.transform.estimate_transform(ttype, src, dst, *args, **kwargs)

src: shape(n,2)
dst: shape(n,2)

'欧式变换'，相似性'，'仿射'，'分段仿射'，'投影'，'多项式'
‘euclidean’, similarity’, ‘affine’, ‘piecewise-affine’, ‘projective’, ‘polynomial’

NAME / TTYPE        FUNCTION PARAMETERS
'euclidean'         `src, `dst`
'similarity'        `src, `dst`
'affine'            `src, `dst`
'piecewise-affine'  `src, `dst`
'projective'        `src, `dst`
'polynomial'        `src, `dst`, `order` (polynomial order,
                                          default order is 2)

tform = transform.estimate_transform('similarity', src, dst)

tform.params: 表示对应的 numpy 矩阵，3*3
```