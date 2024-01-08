#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * print_python_list_info - Function to be built
 * @p: python list
*/
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *list;
	Py_ssize_t allocated;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	list = (PyListObject *) p;
	allocated = list->allocated;
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
