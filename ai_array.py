# Copyright 2020 Autodesk, Inc.  All rights reserved.
#
# Use of this software is subject to the terms of the Autodesk license
# agreement provided at the time of installation or download, or which
# otherwise accompanies this software in either electronic or hard copy form.

import inspect
import sys
from ctypes import *
from .arnold_common import ai, NullToNone, AtNode
from .ai_color import *
from .ai_types import *
from .ai_vector import *
from .ai_matrix import *

class AtArray(Structure):
   pass

ai.AiArray.restype = POINTER(AtArray)

def AiArray(nelems, keys, type, *params):
    return ai.AiArray(nelems, keys, type, *params)

_AiArrayAllocate = ai.AiArrayAllocate
_AiArrayAllocate.argtypes = [c_uint32, c_ubyte, c_ubyte]
_AiArrayAllocate.restype = c_void_p

def AiArrayAllocate(nelements, nkeys, type):
    return NullToNone(_AiArrayAllocate(nelements, nkeys, type), POINTER(AtArray))

AiArrayDestroy = ai.AiArrayDestroy
AiArrayDestroy.argtypes = [POINTER(AtArray)]

_AiArrayConvert = ai.AiArrayConvert
_AiArrayConvert.argtypes = [c_uint32, c_ubyte, c_ubyte, c_void_p]
_AiArrayConvert.restype = c_void_p

def AiArrayConvert(nelements, nkeys, type, data):
    return NullToNone(_AiArrayConvert(nelements, nkeys, type, data), POINTER(AtArray))

AiArrayResize = ai.AiArrayResize
AiArrayResize.argtypes = [POINTER(AtArray), c_uint32, c_ubyte]

_AiArrayCopy = ai.AiArrayCopy
_AiArrayCopy.argtypes = [POINTER(AtArray)]
_AiArrayCopy.restype = c_void_p

def AiArrayCopy(array):
    return NullToNone(_AiArrayCopy(array), POINTER(AtArray))

AiArraySetKey = ai.AiArraySetKey
AiArraySetKey.argtypes = [POINTER(AtArray), c_ubyte, c_void_p]
AiArraySetKey.restype = c_bool

AiArrayMap = ai.AiArrayMap
AiArrayMap.argtypes = [POINTER(AtArray)]
AiArrayMap.restype = c_void_p

AiArrayMapKey = ai.AiArrayMapKey
AiArrayMapKey.argtypes = [POINTER(AtArray), c_ubyte]
AiArrayMapKey.restype = c_void_p

AiArrayUnmap = ai.AiArrayUnmap
AiArrayUnmap.argtypes = [POINTER(AtArray)]

AiArrayGetNumElements = ai.AiArrayGetNumElements
AiArrayGetNumElements.argtypes = [POINTER(AtArray)]
AiArrayGetNumElements.restype = c_uint32

AiArrayGetNumKeys = ai.AiArrayGetNumKeys
AiArrayGetNumKeys.argtypes = [POINTER(AtArray)]
AiArrayGetNumKeys.restype = c_ubyte

AiArrayGetType = ai.AiArrayGetType
AiArrayGetType.argtypes = [POINTER(AtArray)]
AiArrayGetType.restype = c_ubyte

AiArrayGetDataSize = ai.AiArrayGetDataSize
AiArrayGetDataSize.argtypes = [POINTER(AtArray)]
AiArrayGetDataSize.restype = c_size_t

AiArrayGetKeySize = ai.AiArrayGetKeySize
AiArrayGetKeySize.argtypes = [POINTER(AtArray)]
AiArrayGetKeySize.restype = c_size_t

AiArrayInterpolateVec = ai.AiArrayInterpolateVec
AiArrayInterpolateVec.argtypes = [POINTER(AtArray), c_float, c_uint32]
AiArrayInterpolateVec.restype = AtVector

AiArrayInterpolateFlt = ai.AiArrayInterpolateFlt
AiArrayInterpolateFlt.argtypes = [POINTER(AtArray), c_float, c_uint32]
AiArrayInterpolateFlt.restype = c_float

AiArrayInterpolateRGB = ai.AiArrayInterpolateRGB
AiArrayInterpolateRGB.argtypes = [POINTER(AtArray), c_float, c_uint32]
AiArrayInterpolateRGB.restype = AtRGB

AiArrayInterpolateRGBA = ai.AiArrayInterpolateRGBA
AiArrayInterpolateRGBA.argtypes = [POINTER(AtArray), c_float, c_uint32]
AiArrayInterpolateRGBA.restype = AtRGBA

AiArrayInterpolateMtx = ai.AiArrayInterpolateMtx
AiArrayInterpolateMtx.argtypes = [POINTER(AtArray), c_float, c_uint32]
AiArrayInterpolateMtx.restype = AtMatrix

# AtArray getters
#
_AiArrayGetBool = ai.AiArrayGetBoolFunc
_AiArrayGetBool.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetBool.restype = c_bool

def AiArrayGetBool(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArrayGetBool(array, index, filename, lineno)
    except:
        return _AiArrayGetBool(array, index, "<unknown>", 0)

_AiArrayGetByte = ai.AiArrayGetByteFunc
_AiArrayGetByte.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetByte.restype = c_ubyte

def AiArrayGetByte(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArrayGetByte(array, index, filename, lineno)
    except:
        return _AiArrayGetByte(array, index, "<unknown>", 0)

_AiArrayGetInt = ai.AiArrayGetIntFunc
_AiArrayGetInt.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetInt.restype = c_int

def AiArrayGetInt(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArrayGetInt(array, index, filename, lineno)
    except:
        return _AiArrayGetInt(array, index, "<unknown>", 0)

_AiArrayGetUInt = ai.AiArrayGetUIntFunc
_AiArrayGetUInt.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetUInt.restype = c_uint

def AiArrayGetUInt(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArrayGetUInt(array, index, filename, lineno)
    except:
        return _AiArrayGetUInt(array, index, "<unknown>", 0)

_AiArrayGetFlt = ai.AiArrayGetFltFunc
_AiArrayGetFlt.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetFlt.restype = c_float

def AiArrayGetFlt(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArrayGetFlt(array, index, filename, lineno)
    except:
        return _AiArrayGetFlt(array, index, "<unknown>", 0)

_AiArrayGetVec2 = ai.AiArrayGetVec2Func
_AiArrayGetVec2.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
if return_small_struct_exception:
    _AiArrayGetVec2.restype = AtVector
    def AiArrayGetVec2(array, index):
        try:
            (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
            tmp = _AiArrayGetVec2(array, index, filename, lineno)
        except:
            tmp = _AiArrayGetVec2(array, index, "<unknown>", 0)
        return AtVector2(tmp.x, tmp.y)
else:
    _AiArrayGetVec2.restype = AtVector2
    def AiArrayGetVec2(array, index):
        try:
            (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
            return _AiArrayGetVec2(array, index, filename, lineno)
        except:
            return _AiArrayGetVec2(array, index, "<unknown>", 0)

_AiArrayGetVec = ai.AiArrayGetVecFunc
_AiArrayGetVec.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetVec.restype = AtVector

def AiArrayGetVec(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArrayGetVec(array, index, filename, lineno)
    except:
        return _AiArrayGetVec(array, index, "<unknown>", 0)

_AiArrayGetRGB = ai.AiArrayGetRGBFunc
_AiArrayGetRGB.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetRGB.restype = AtRGB

def AiArrayGetRGB(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArrayGetRGB(array, index, filename, lineno)
    except:
        return _AiArrayGetRGB(array, index, "<unknown>", 0)

_AiArrayGetRGBA = ai.AiArrayGetRGBAFunc
_AiArrayGetRGBA.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetRGBA.restype = AtRGBA

def AiArrayGetRGBA(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArrayGetRGBA(array, index, filename, lineno)
    except:
        return _AiArrayGetRGBA(array, index, "<unknown>", 0)

_AiArrayGetPtr = ai.AiArrayGetPtrFunc
_AiArrayGetPtr.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetPtr.restype = c_void_p

def AiArrayGetPtr(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return NullToNone(_AiArrayGetPtr(array, index, filename, lineno), POINTER(AtNode))
    except:
        return NullToNone(_AiArrayGetPtr(array, index, "<unknown>", 0), POINTER(AtNode))

_AiArrayGetStr = ai.AiArrayGetStrFunc
_AiArrayGetStr.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetStr.restype = AtStringReturn

def AiArrayGetStr(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return AtStringToStr(_AiArrayGetStr(array, index, filename, lineno))
    except:
        return AtStringToStr(_AiArrayGetStr(array, index, "<unknown>", 0))

_AiArrayGetArray = ai.AiArrayGetArrayFunc
_AiArrayGetArray.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetArray.restype = c_void_p

def AiArrayGetArray(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return NullToNone(_AiArrayGetArray(array, index, filename, lineno), POINTER(AtArray))
    except:
        return NullToNone(_AiArrayGetArray(array, index, "<unknown>", 0), POINTER(AtArray))

_AiArrayGetMtx = ai.AiArrayGetMtxFunc
_AiArrayGetMtx.argtypes = [POINTER(AtArray), c_uint32, AtPythonString, c_int]
_AiArrayGetMtx.restype = AtMatrix

def AiArrayGetMtx(array, index):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArrayGetMtx(array, index, filename, lineno)
    except:
        return _AiArrayGetMtx(array, index, "<unknown>", 0)

# AtArray setters
#

_AiArraySetBool = ai.AiArraySetBoolFunc
_AiArraySetBool.argtypes = [POINTER(AtArray), c_uint32, c_bool, AtPythonString, c_int]
_AiArraySetBool.restype = c_bool

def AiArraySetBool(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetBool(array, index, value, filename, lineno)
    except:
        return _AiArraySetBool(array, index, value, "<unknown>", 0)

_AiArraySetByte = ai.AiArraySetByteFunc
_AiArraySetByte.argtypes = [POINTER(AtArray), c_uint32, c_ubyte, AtPythonString, c_int]
_AiArraySetByte.restype = c_bool

def AiArraySetByte(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetByte(array, index, value, filename, lineno)
    except:
        return _AiArraySetByte(array, index, value, "<unknown>", 0)

_AiArraySetInt = ai.AiArraySetIntFunc
_AiArraySetInt.argtypes = [POINTER(AtArray), c_uint32, c_int, AtPythonString, c_int]
_AiArraySetInt.restype = c_bool

def AiArraySetInt(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetInt(array, index, value, filename, lineno)
    except:
        return _AiArraySetInt(array, index, value, "<unknown>", 0)

_AiArraySetUInt = ai.AiArraySetUIntFunc
_AiArraySetUInt.argtypes = [POINTER(AtArray), c_uint32, c_uint, AtPythonString, c_int]
_AiArraySetUInt.restype = c_bool

def AiArraySetUInt(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetUInt(array, index, value, filename, lineno)
    except:
        return _AiArraySetUInt(array, index, value, "<unknown>", 0)

_AiArraySetFlt = ai.AiArraySetFltFunc
_AiArraySetFlt.argtypes = [POINTER(AtArray), c_uint32, c_float, AtPythonString, c_int]
_AiArraySetFlt.restype = c_bool

def AiArraySetFlt(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetFlt(array, index, value, filename, lineno)
    except:
        return _AiArraySetFlt(array, index, value, "<unknown>", 0)

_AiArraySetRGB = ai.AiArraySetRGBFunc
_AiArraySetRGB.argtypes = [POINTER(AtArray), c_uint32, AtRGB, AtPythonString, c_int]
_AiArraySetRGB.restype = c_bool

def AiArraySetRGB(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetRGB(array, index, value, filename, lineno)
    except:
        return _AiArraySetRGB(array, index, value, "<unknown>", 0)

_AiArraySetRGBA = ai.AiArraySetRGBAFunc
_AiArraySetRGBA.argtypes = [POINTER(AtArray), c_uint32, AtRGBA, AtPythonString, c_int]
_AiArraySetRGBA.restype = c_bool

def AiArraySetRGBA(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetRGBA(array, index, value, filename, lineno)
    except:
        return _AiArraySetRGBA(array, index, value, "<unknown>", 0)

_AiArraySetVec2 = ai.AiArraySetVec2Func
_AiArraySetVec2.argtypes = [POINTER(AtArray), c_uint32, AtVector2, AtPythonString, c_int]
_AiArraySetVec2.restype = c_bool

def AiArraySetVec2(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetVec2(array, index, value, filename, lineno)
    except:
        return _AiArraySetVec2(array, index, value, "<unknown>", 0)

_AiArraySetVec = ai.AiArraySetVecFunc
_AiArraySetVec.argtypes = [POINTER(AtArray), c_uint32, AtVector, AtPythonString, c_int]
_AiArraySetVec.restype = c_bool

def AiArraySetVec(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetVec(array, index, value, filename, lineno)
    except:
        return _AiArraySetVec(array, index, value, "<unknown>", 0)

_AiArraySetMtx = ai.AiArraySetMtxFunc
_AiArraySetMtx.argtypes = [POINTER(AtArray), c_uint32, AtMatrix, AtPythonString, c_int]
_AiArraySetMtx.restype = c_bool

def AiArraySetMtx(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetMtx(array, index, value, filename, lineno)
    except:
        return _AiArraySetMtx(array, index, value, "<unknown>", 0)

_AiArraySetStr = ai.AiArraySetStrFunc
_AiArraySetStr.argtypes = [POINTER(AtArray), c_uint32, AtString, AtPythonString, c_int]
_AiArraySetStr.restype = c_bool

def AiArraySetStr(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetStr(array, index, value, filename, lineno)
    except:
        return _AiArraySetStr(array, index, value, "<unknown>", 0)

_AiArraySetPtr = ai.AiArraySetPtrFunc
_AiArraySetPtr.argtypes = [POINTER(AtArray), c_uint32, c_void_p, AtPythonString, c_int]
_AiArraySetPtr.restype = c_bool

def AiArraySetPtr(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetPtr(array, index, value, filename, lineno)
    except:
        return _AiArraySetPtr(array, index, value, "<unknown>", 0)

_AiArraySetArray = ai.AiArraySetArrayFunc
_AiArraySetArray.argtypes = [POINTER(AtArray), c_uint32, POINTER(AtArray), AtPythonString, c_int]
_AiArraySetArray.restype = c_bool

def AiArraySetArray(array, index, value):
    try:
        (filename, lineno, fnc, ctx, fidx) = inspect.getframeinfo(sys._getframe(1))
        return _AiArraySetArray(array, index, value, filename, lineno)
    except:
        return _AiArraySetArray(array, index, value, "<unknown>", 0)
