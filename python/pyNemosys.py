# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyNemosys', [dirname(__file__)])
        except ImportError:
            import _pyNemosys
            return _pyNemosys
        if fp is not None:
            try:
                _mod = imp.load_module('_pyNemosys', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyNemosys = swig_import_helper()
    del swig_import_helper
else:
    import _pyNemosys
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyNemosys.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self) -> "PyObject *":
        return _pyNemosys.SwigPyIterator_value(self)

    def incr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _pyNemosys.SwigPyIterator_incr(self, n)

    def decr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _pyNemosys.SwigPyIterator_decr(self, n)

    def distance(self, x: 'SwigPyIterator') -> "ptrdiff_t":
        return _pyNemosys.SwigPyIterator_distance(self, x)

    def equal(self, x: 'SwigPyIterator') -> "bool":
        return _pyNemosys.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _pyNemosys.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _pyNemosys.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _pyNemosys.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _pyNemosys.SwigPyIterator_previous(self)

    def advance(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _pyNemosys.SwigPyIterator_advance(self, n)

    def __eq__(self, x: 'SwigPyIterator') -> "bool":
        return _pyNemosys.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: 'SwigPyIterator') -> "bool":
        return _pyNemosys.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _pyNemosys.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _pyNemosys.SwigPyIterator___isub__(self, n)

    def __add__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _pyNemosys.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _pyNemosys.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pyNemosys.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vectorString(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorString, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorString, name)
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _pyNemosys.vectorString_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _pyNemosys.vectorString___nonzero__(self)

    def __bool__(self) -> "bool":
        return _pyNemosys.vectorString___bool__(self)

    def __len__(self) -> "std::vector< std::string >::size_type":
        return _pyNemosys.vectorString___len__(self)

    def __getslice__(self, i: 'std::vector< std::string >::difference_type', j: 'std::vector< std::string >::difference_type') -> "std::vector< std::string,std::allocator< std::string > > *":
        return _pyNemosys.vectorString___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _pyNemosys.vectorString___setslice__(self, *args)

    def __delslice__(self, i: 'std::vector< std::string >::difference_type', j: 'std::vector< std::string >::difference_type') -> "void":
        return _pyNemosys.vectorString___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _pyNemosys.vectorString___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< std::string >::value_type const &":
        return _pyNemosys.vectorString___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _pyNemosys.vectorString___setitem__(self, *args)

    def pop(self) -> "std::vector< std::string >::value_type":
        return _pyNemosys.vectorString_pop(self)

    def append(self, x: 'std::vector< std::string >::value_type const &') -> "void":
        return _pyNemosys.vectorString_append(self, x)

    def empty(self) -> "bool":
        return _pyNemosys.vectorString_empty(self)

    def size(self) -> "std::vector< std::string >::size_type":
        return _pyNemosys.vectorString_size(self)

    def swap(self, v: 'vectorString') -> "void":
        return _pyNemosys.vectorString_swap(self, v)

    def begin(self) -> "std::vector< std::string >::iterator":
        return _pyNemosys.vectorString_begin(self)

    def end(self) -> "std::vector< std::string >::iterator":
        return _pyNemosys.vectorString_end(self)

    def rbegin(self) -> "std::vector< std::string >::reverse_iterator":
        return _pyNemosys.vectorString_rbegin(self)

    def rend(self) -> "std::vector< std::string >::reverse_iterator":
        return _pyNemosys.vectorString_rend(self)

    def clear(self) -> "void":
        return _pyNemosys.vectorString_clear(self)

    def get_allocator(self) -> "std::vector< std::string >::allocator_type":
        return _pyNemosys.vectorString_get_allocator(self)

    def pop_back(self) -> "void":
        return _pyNemosys.vectorString_pop_back(self)

    def erase(self, *args) -> "std::vector< std::string >::iterator":
        return _pyNemosys.vectorString_erase(self, *args)

    def __init__(self, *args):
        this = _pyNemosys.new_vectorString(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x: 'std::vector< std::string >::value_type const &') -> "void":
        return _pyNemosys.vectorString_push_back(self, x)

    def front(self) -> "std::vector< std::string >::value_type const &":
        return _pyNemosys.vectorString_front(self)

    def back(self) -> "std::vector< std::string >::value_type const &":
        return _pyNemosys.vectorString_back(self)

    def assign(self, n: 'std::vector< std::string >::size_type', x: 'std::vector< std::string >::value_type const &') -> "void":
        return _pyNemosys.vectorString_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _pyNemosys.vectorString_resize(self, *args)

    def insert(self, *args) -> "void":
        return _pyNemosys.vectorString_insert(self, *args)

    def reserve(self, n: 'std::vector< std::string >::size_type') -> "void":
        return _pyNemosys.vectorString_reserve(self, n)

    def capacity(self) -> "std::vector< std::string >::size_type":
        return _pyNemosys.vectorString_capacity(self)
    __swig_destroy__ = _pyNemosys.delete_vectorString
    __del__ = lambda self: None
vectorString_swigregister = _pyNemosys.vectorString_swigregister
vectorString_swigregister(vectorString)

class meshBase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, meshBase, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, meshBase, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _pyNemosys.new_meshBase()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pyNemosys.delete_meshBase
    __del__ = lambda self: None
    __swig_getmethods__["Create"] = lambda x: _pyNemosys.meshBase_Create
    if _newclass:
        Create = staticmethod(_pyNemosys.meshBase_Create)
    __swig_getmethods__["CreateShared"] = lambda x: _pyNemosys.meshBase_CreateShared
    if _newclass:
        CreateShared = staticmethod(_pyNemosys.meshBase_CreateShared)

    def getPoint(self, id: 'int') -> "std::vector< double,std::allocator< double > >":
        return _pyNemosys.meshBase_getPoint(self, id)

    def getCell(self, id: 'int') -> "std::map< int,std::vector< double,std::allocator< double > > >":
        return _pyNemosys.meshBase_getCell(self, id)

    def getCellVec(self, id: 'int') -> "std::vector< std::vector< double,std::allocator< double > >,std::allocator< std::vector< double,std::allocator< double > > > >":
        return _pyNemosys.meshBase_getCellVec(self, id)

    def getDataSet(self) -> "vtkSmartPointer< vtkDataSet >":
        return _pyNemosys.meshBase_getDataSet(self)

    def setPointDataArray(self, name: 'char const *', data: 'std::vector< std::vector< double,std::allocator< double > >,std::allocator< std::vector< double,std::allocator< double > > > > const &') -> "void":
        return _pyNemosys.meshBase_setPointDataArray(self, name, data)

    def setCellDataArray(self, *args) -> "void":
        return _pyNemosys.meshBase_setCellDataArray(self, *args)

    def unsetPointDataArray(self, *args) -> "void":
        return _pyNemosys.meshBase_unsetPointDataArray(self, *args)

    def unsetCellDataArray(self, *args) -> "void":
        return _pyNemosys.meshBase_unsetCellDataArray(self, *args)

    def unsetFieldDataArray(self, name: 'char const *') -> "void":
        return _pyNemosys.meshBase_unsetFieldDataArray(self, name)

    def getCellLengths(self) -> "std::vector< double,std::allocator< double > >":
        return _pyNemosys.meshBase_getCellLengths(self)

    def getCellCenter(self, cellID: 'int') -> "std::vector< double,std::allocator< double > >":
        return _pyNemosys.meshBase_getCellCenter(self, cellID)

    def buildLocator(self) -> "vtkSmartPointer< vtkCellLocator >":
        return _pyNemosys.meshBase_buildLocator(self)

    def getIntegrationPointsAtCell(self, cellID: 'int') -> "void":
        return _pyNemosys.meshBase_getIntegrationPointsAtCell(self, cellID)

    def transfer(self, *args) -> "int":
        return _pyNemosys.meshBase_transfer(self, *args)

    def generateSizeField(self, method: 'std::string', arrayID: 'int', dev_mlt: 'double', maxIsmin: 'bool') -> "void":
        return _pyNemosys.meshBase_generateSizeField(self, method, arrayID, dev_mlt, maxIsmin)

    def setSFBool(self, q: 'bool') -> "void":
        return _pyNemosys.meshBase_setSFBool(self, q)

    def getSFBool(self) -> "bool":
        return _pyNemosys.meshBase_getSFBool(self)

    def IsArrayName(self, name: 'std::string') -> "int":
        return _pyNemosys.meshBase_IsArrayName(self, name)

    def refineMesh(self, *args) -> "void":
        return _pyNemosys.meshBase_refineMesh(self, *args)

    def report(self) -> "void":
        return _pyNemosys.meshBase_report(self)

    def getNumberOfPoints(self) -> "int":
        return _pyNemosys.meshBase_getNumberOfPoints(self)

    def getNumberOfCells(self) -> "int":
        return _pyNemosys.meshBase_getNumberOfCells(self)

    def checkMesh(self, ofname: 'std::string') -> "void":
        return _pyNemosys.meshBase_checkMesh(self, ofname)

    def write(self, *args) -> "void":
        return _pyNemosys.meshBase_write(self, *args)

    def writeMSH(self, *args) -> "void":
        return _pyNemosys.meshBase_writeMSH(self, *args)

    def setFileName(self, fname: 'std::string') -> "void":
        return _pyNemosys.meshBase_setFileName(self, fname)

    def getFileName(self) -> "std::string":
        return _pyNemosys.meshBase_getFileName(self)

    def setCheckQuality(self, x: 'bool') -> "void":
        return _pyNemosys.meshBase_setCheckQuality(self, x)
meshBase_swigregister = _pyNemosys.meshBase_swigregister
meshBase_swigregister(meshBase)

def meshBase_Create(fname: 'std::string') -> "meshBase *":
    return _pyNemosys.meshBase_Create(fname)
meshBase_Create = _pyNemosys.meshBase_Create

def meshBase_CreateShared(fname: 'std::string') -> "std::shared_ptr< meshBase >":
    return _pyNemosys.meshBase_CreateShared(fname)
meshBase_CreateShared = _pyNemosys.meshBase_CreateShared


def diffMesh(mesh1: 'meshBase', mesh2: 'meshBase') -> "int":
    return _pyNemosys.diffMesh(mesh1, mesh2)
diffMesh = _pyNemosys.diffMesh
# This file is compatible with both classic and new-style classes.


