#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <Python.h>

#define MAX_JSON_LEN 4096


PyObject* cjson_loads(PyObject *self, PyObject *args)
{
    const char *string;
    if (!PyArg_ParseTuple(args, "s", &string))
    {
        PyErr_Format(PyExc_TypeError, "Expected string as argument");
        return NULL;
    }

    char *json_string = NULL;
    if (!(json_string = strdup(string)))
    {
        PyErr_Format(PyExc_ValueError, "Failed to create string copy");
        return NULL;
    }
    char *string_pointer = json_string;

    json_string++;
    long len = strlen(json_string);
    json_string[len - 1] = '\0';

    PyObject *dict = NULL;
    if (!(dict = PyDict_New()))
    {
        PyErr_Format(PyExc_ValueError, "Failed to create Dict Object");
        return NULL;
    }

    PyObject *key = NULL;
    PyObject *value = NULL;

    char *substr = strtok(json_string, ", ");
    int i = 0;
    while (substr != NULL)
    {
        if (i % 2 == 0)
        {
            substr[strlen(substr) - 2] = '\0';
            substr++;
            if (!(key = Py_BuildValue("s", substr)))
            {
                PyErr_Format(PyExc_ValueError, "Failed to build string value");
                return NULL;
            }
        }
        else
        {
            if (substr[0] == '"')
            {
                substr[strlen(substr) - 1] = '\0';
                substr++;
                if (!(value = Py_BuildValue("s", substr)))
                {
                    PyErr_Format(PyExc_ValueError, "Failed to build string value");
                    return NULL;
                }
            }
            else if (!(value = Py_BuildValue("i", atoi(substr))))
            {
                PyErr_Format(PyExc_ValueError, "Failed to build integer value");
                return NULL;
            }

            if (PyDict_SetItem(dict, key, value) < 0)
            {
                PyErr_Format(PyExc_ValueError, "Failed to set item");
                return NULL;
            }
        }

        substr = strtok(NULL, ", ");
        i++;
    }
    free(string_pointer);

    return dict;
}

PyObject* cjson_dumps(PyObject *self, PyObject *args)
{
    PyDictObject *dict_obj;

    if (!PyArg_ParseTuple(args, "O", &dict_obj))
    {
        PyErr_Format(PyExc_TypeError, "Expected dict as argument");
        return NULL;
    }

    PyObject *items = PyDict_Items(dict_obj);
    long list_len = PyList_Size(items);

    PyObject *item, *key, *value;
    char temp_string[MAX_JSON_LEN];
    char json_string[MAX_JSON_LEN];
    char *ckey, *cvalue;
    bool number_flag;
    strcpy(json_string, "{");

    for (long i = 0; i < list_len; ++i)
    {
        item = PyList_GetItem(items, i);
        key = PyTuple_GetItem(item, 0);
        value = PyTuple_GetItem(item, 1);

        number_flag = false;
        if (!PyUnicode_Check(value))
        {
            value = PyObject_Str(value);
            number_flag = true;
        }

        ckey = PyUnicode_AsUTF8(key);
        cvalue = PyUnicode_AsUTF8(value);

        if (number_flag)
            sprintf(temp_string, "\"%s\": %s", ckey, cvalue);
        else
            sprintf(temp_string, "\"%s\": \"%s\"", ckey, cvalue);

        strcat(json_string, temp_string);
        if (i != list_len - 1)
            strcat(json_string, ", ");
    }

    strcat(json_string, "}");

    return Py_BuildValue("s", json_string);
}

static PyMethodDef methods[] = {
    {"loads", cjson_loads, METH_VARARGS, NULL},
    {"dumps", cjson_dumps, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef cjson_module = {
    PyModuleDef_HEAD_INIT,
    "cjson",
    "Module for json parsing and serializing.",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_cjson(void)
{
    return PyModule_Create( &cjson_module );
}
