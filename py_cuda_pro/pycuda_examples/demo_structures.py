
from pycuda.compiler import SourceModule

mod = SourceModule("""'
    Struct DoubleOperation{
    int datalen, __padding;
    float *ptr;
    }
    __global__ void double_array(DoubleOperation *a) {
        a = &a[blockIdx.x]
        for (int idx = threadIdx.x; idx <a ->datalen; idx += blocDim.x) {
            a ->ptr[idx] *= 2
        }
    }   
""")