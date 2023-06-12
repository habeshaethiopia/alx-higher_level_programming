#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - the fuction
 * @p: the pyObject
 *
 */
void print_python_list_info(PyObject *p)
{
	long int n, A;
	PyObject *pyitem;

	n = PyList_Size(p);
	A = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", n);
	printf("[*] Allocated = %ld\n", A);

	for (int i = 0; i < n; i++)
	{
		pyitem = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(pyitem)->tp_name);
	}
}
