#include <Python.h>

void print_python_string(PyObject *p)
{
	PyObject *bytes = NULL;
	const char *str = NULL;

	if (PyUnicode_Check(p))
	{
		bytes = PyUnicode_AsUTF8String(p);
		str = PyBytes_AsString(bytes);
		printf("%s\n", str);
		Py_DECREF(bytes);
	}
	else
		PyErr_SetString(PyExc_TypeError, "Invalid String Object");
