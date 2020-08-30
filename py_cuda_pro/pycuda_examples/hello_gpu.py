#import pycuda.autoint
#import pycuda.driver as drv
import numpy


from pycuda.compiler  import SourceModule

mod = SourceModule("""
__global__ void multiply_them(float *dest, float *a, float *b)
{
    const int i = threadIdx.x;
    dest[i] = a[i] * b[i];
}

""")

multiply_them = mod.get_function("multiply_them")

a = numpy.random.randn(400).astype(numpy.float32)
b = numpy.random.randn(400).astype(numpy.float32)

dest = numpy.zeros_like(a)
multiply_them(
    drv.Out(dest), drv.In(a), drv.In(b),
    block=(400, 1,1 ), grid=(1,1)
)
print dest-a*b

# ----------------------------------
a = numpy.random.rand(4, 4)
a = a.astype(numpy.float32)
a_gpu = cuda.mem_alloc(a.nbytes)
# We need to transfor the data to the GPU
# cud.memcpy_htod(a_gpu, a)
func = mod.get_function("doublify")
func(a_gpu, block=(4, 4, 1))
# shortcut
#func(cuda.InOut(a), block()4, 4, 1)

a_doubled = numpy.empt_like(a)
cuda.memcpy_htod(a_doubled, a_gpu)
print("a doubled : ", a_doubled)
print("a :" , a)

# Same effect with less writing
import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoint
import numpy
a_gpu = gpuarray.to_gpu(numpy.random.randn(4,4).astype(numpy.float32))
a_doubled = (2*a_gpu).get()
print(a_doubled)
print(a)