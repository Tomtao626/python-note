/* example.i */
%module example
%{
/* Put header files here or function declarations like below */
extern double My_variable;
extern int fact(int n);
extern int my_mod(int x, int y);
extern char *get_time();
%}

extern double My_variable;
extern int fact(int n);
extern int my_mod(int x, int y);
extern char *get_time();


/*
第 1 行，我们定义了模块的名称为 example。
第 2-8 行，我们直接指定了example.c中的函数定义，也可以定义一个example.h头文件，并将这些定义加入其中；然后，在 %{ … %}结构体中包含example.h，来实现相同的功能。
第10-13行，则是定义了导出的接口，以便你在 Python 中直接调用这些接口。
*/