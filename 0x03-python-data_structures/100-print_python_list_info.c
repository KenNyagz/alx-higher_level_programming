#include <Python.h>
#include <stdio.h>


void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject) *p;
    Py_ssize_t size = PyList_Size(p), i = 0;
    const char *type_name;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = Pylist_GetItem(p, i);
        type_name = Py_TYPE(item)->tp_name;
        printf("Element %ld: %s\n", i, type_name);
     }

}
