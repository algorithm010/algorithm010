学习笔记
判断奇偶 
x&1 == 1 if odd else even
x = x & (x-1) 清除最右的1
x = x & (-x) 得到最右的1