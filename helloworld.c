#include <Python.h>

static PyObject*
helloworld(PyObject* self)
{
    return Py_BuildValue("s", "Hello, World!");
}

static char helloworld_docs[] = "\
helloworld(): prints 'Hello, World!'\n\
";

static PyMethodDef helloworld_funcs[] = {
    {"helloworld", (PyCFunction)helloworld, METH_NOARGS, helloworld_docs},
    {NULL}
};

static char helloworld_module_docs[] = "Module used to print Hello, World!";

static struct PyModuleDef helloworld_module = {
	PyModuleDef_HEAD_INIT,
	"helloworld",
	helloworld_module_docs,
	-1,
	helloworld_funcs
};

PyMODINIT_FUNC
PyInit_helloworld(void){
    PyObject* m = PyModule_Create(&helloworld_module);
    return m;
}
