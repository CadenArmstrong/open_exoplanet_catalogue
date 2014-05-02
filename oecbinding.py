# ./oecbinding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-05-02 12:57:21.966608 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d3fecb94-d21a-11e3-a824-0021cccb898d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: empty-string
class empty_string (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'empty-string')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 105, 1)
    _Documentation = None
empty_string._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=empty_string, enum_prefix=None)
empty_string.emptyString = empty_string._CF_enumeration.addEnumeration(unicode_value=u'', tag='emptyString')
empty_string._InitializeFacetMap(empty_string._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'empty-string', empty_string)

# Atomic simple type: spectraltypedef
class spectraltypedef (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectraltypedef')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 127, 1)
    _Documentation = None
spectraltypedef._CF_pattern = pyxb.binding.facets.CF_pattern()
spectraltypedef._CF_pattern.addPattern(pattern=u'[OBAFGKMLTYRNS].*')
spectraltypedef._InitializeFacetMap(spectraltypedef._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'spectraltypedef', spectraltypedef)

# Atomic simple type: rightascensiondef
class rightascensiondef (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rightascensiondef')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 133, 1)
    _Documentation = None
rightascensiondef._CF_pattern = pyxb.binding.facets.CF_pattern()
rightascensiondef._CF_pattern.addPattern(pattern=u'[0-2]\\d [0-5]\\d [0-5]\\d(\\.\\d{2}){0,1}')
rightascensiondef._InitializeFacetMap(rightascensiondef._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'rightascensiondef', rightascensiondef)

# Atomic simple type: declinationdef
class declinationdef (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'declinationdef')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 139, 1)
    _Documentation = None
declinationdef._CF_pattern = pyxb.binding.facets.CF_pattern()
declinationdef._CF_pattern.addPattern(pattern=u'(\\+|\\-)(\\d{2} [0-5]\\d [0-5]\\d)(\\.\\d{2}){0,1}')
declinationdef._InitializeFacetMap(declinationdef._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'declinationdef', declinationdef)

# Atomic simple type: datetime
class datetime (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'datetime')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 145, 1)
    _Documentation = None
datetime._CF_pattern = pyxb.binding.facets.CF_pattern()
datetime._CF_pattern.addPattern(pattern=u'\\d{2}/[0-1]\\d/[0-3]\\d')
datetime._InitializeFacetMap(datetime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'datetime', datetime)

# Atomic simple type: listtype
class listtype (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listtype')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 151, 1)
    _Documentation = None
listtype._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=listtype, enum_prefix=None)
listtype.Confirmed_planets = listtype._CF_enumeration.addEnumeration(unicode_value=u'Confirmed planets', tag=u'Confirmed_planets')
listtype.Not_confirmed_planets = listtype._CF_enumeration.addEnumeration(unicode_value=u'Not confirmed planets', tag=u'Not_confirmed_planets')
listtype.Planets_in_binary_systems_S_type = listtype._CF_enumeration.addEnumeration(unicode_value=u'Planets in binary systems, S-type', tag=u'Planets_in_binary_systems_S_type')
listtype.Planets_in_binary_systems_P_type = listtype._CF_enumeration.addEnumeration(unicode_value=u'Planets in binary systems, P-type', tag=u'Planets_in_binary_systems_P_type')
listtype.Orphan_planets = listtype._CF_enumeration.addEnumeration(unicode_value=u'Orphan planets', tag=u'Orphan_planets')
listtype.Controversial = listtype._CF_enumeration.addEnumeration(unicode_value=u'Controversial', tag=u'Controversial')
listtype.Solar_System = listtype._CF_enumeration.addEnumeration(unicode_value=u'Solar System', tag=u'Solar_System')
listtype.Kepler_Objects_of_Interest = listtype._CF_enumeration.addEnumeration(unicode_value=u'Kepler Objects of Interest', tag=u'Kepler_Objects_of_Interest')
listtype._InitializeFacetMap(listtype._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'listtype', listtype)

# Atomic simple type: discoverymethodtype
class discoverymethodtype (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'discoverymethodtype')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 164, 1)
    _Documentation = None
discoverymethodtype._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=discoverymethodtype, enum_prefix=None)
discoverymethodtype.imaging = discoverymethodtype._CF_enumeration.addEnumeration(unicode_value=u'imaging', tag=u'imaging')
discoverymethodtype.microlensing = discoverymethodtype._CF_enumeration.addEnumeration(unicode_value=u'microlensing', tag=u'microlensing')
discoverymethodtype.RV = discoverymethodtype._CF_enumeration.addEnumeration(unicode_value=u'RV', tag=u'RV')
discoverymethodtype.timing = discoverymethodtype._CF_enumeration.addEnumeration(unicode_value=u'timing', tag=u'timing')
discoverymethodtype.transit = discoverymethodtype._CF_enumeration.addEnumeration(unicode_value=u'transit', tag=u'transit')
discoverymethodtype._InitializeFacetMap(discoverymethodtype._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'discoverymethodtype', discoverymethodtype)

# Atomic simple type: year
class year (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'year')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 174, 1)
    _Documentation = None
year._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=year, value=pyxb.binding.datatypes.integer(2020L))
year._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=year, value=pyxb.binding.datatypes.integer(1781L))
year._InitializeFacetMap(year._CF_maxInclusive,
   year._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'year', year)

# Atomic simple type: positiveinteger
class positiveinteger (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positiveinteger')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 181, 1)
    _Documentation = None
positiveinteger._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveinteger, value=pyxb.binding.datatypes.nonNegativeInteger(0L))
positiveinteger._InitializeFacetMap(positiveinteger._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'positiveinteger', positiveinteger)

# Atomic simple type: positivedouble
class positivedouble (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positivedouble')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 187, 1)
    _Documentation = None
positivedouble._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positivedouble, value=pyxb.binding.datatypes.double(0.0))
positivedouble._InitializeFacetMap(positivedouble._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'positivedouble', positivedouble)

# Atomic simple type: webreference
class webreference (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'webreference')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 193, 1)
    _Documentation = None
webreference._CF_pattern = pyxb.binding.facets.CF_pattern()
webreference._CF_pattern.addPattern(pattern=u'https{0,1}://.*')
webreference._InitializeFacetMap(webreference._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'webreference', webreference)

# Union simple type: number-or-empty
# superclasses pyxb.binding.datatypes.anySimpleType
class number_or_empty (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.double, empty_string."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'number-or-empty')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 111, 1)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.double, empty_string, )
number_or_empty._CF_pattern = pyxb.binding.facets.CF_pattern()
number_or_empty._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=number_or_empty)
number_or_empty.emptyString = u''                 # originally empty_string.emptyString
number_or_empty._InitializeFacetMap(number_or_empty._CF_pattern,
   number_or_empty._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'number-or-empty', number_or_empty)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_CTD_ANON_name', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 7, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element spectraltype uses Python identifier spectraltype
    __spectraltype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'spectraltype'), 'spectraltype', '__AbsentNamespace0_CTD_ANON_spectraltype', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 11, 4), )

    
    spectraltype = property(__spectraltype.value, __spectraltype.set, None, None)

    
    # Element rightascension uses Python identifier rightascension
    __rightascension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'rightascension'), 'rightascension', '__AbsentNamespace0_CTD_ANON_rightascension', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 12, 4), )

    
    rightascension = property(__rightascension.value, __rightascension.set, None, None)

    
    # Element declination uses Python identifier declination
    __declination = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'declination'), 'declination', '__AbsentNamespace0_CTD_ANON_declination', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 13, 4), )

    
    declination = property(__declination.value, __declination.set, None, None)

    
    # Element distance uses Python identifier distance
    __distance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'distance'), 'distance', '__AbsentNamespace0_CTD_ANON_distance', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 14, 4), )

    
    distance = property(__distance.value, __distance.set, None, None)

    
    # Element epoch uses Python identifier epoch
    __epoch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'epoch'), 'epoch', '__AbsentNamespace0_CTD_ANON_epoch', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 15, 4), )

    
    epoch = property(__epoch.value, __epoch.set, None, None)

    
    # Element videolink uses Python identifier videolink
    __videolink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'videolink'), 'videolink', '__AbsentNamespace0_CTD_ANON_videolink', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 16, 4), )

    
    videolink = property(__videolink.value, __videolink.set, None, None)

    
    # Element magB uses Python identifier magB
    __magB = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magB'), 'magB', '__AbsentNamespace0_CTD_ANON_magB', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 17, 4), )

    
    magB = property(__magB.value, __magB.set, None, None)

    
    # Element magV uses Python identifier magV
    __magV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magV'), 'magV', '__AbsentNamespace0_CTD_ANON_magV', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 18, 4), )

    
    magV = property(__magV.value, __magV.set, None, None)

    
    # Element magI uses Python identifier magI
    __magI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magI'), 'magI', '__AbsentNamespace0_CTD_ANON_magI', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 19, 4), )

    
    magI = property(__magI.value, __magI.set, None, None)

    
    # Element magJ uses Python identifier magJ
    __magJ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magJ'), 'magJ', '__AbsentNamespace0_CTD_ANON_magJ', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 20, 4), )

    
    magJ = property(__magJ.value, __magJ.set, None, None)

    
    # Element magH uses Python identifier magH
    __magH = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magH'), 'magH', '__AbsentNamespace0_CTD_ANON_magH', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 21, 4), )

    
    magH = property(__magH.value, __magH.set, None, None)

    
    # Element magK uses Python identifier magK
    __magK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magK'), 'magK', '__AbsentNamespace0_CTD_ANON_magK', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 22, 4), )

    
    magK = property(__magK.value, __magK.set, None, None)

    
    # Element magR uses Python identifier magR
    __magR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magR'), 'magR', '__AbsentNamespace0_CTD_ANON_magR', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 23, 4), )

    
    magR = property(__magR.value, __magR.set, None, None)

    
    # Element planet uses Python identifier planet
    __planet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'planet'), 'planet', '__AbsentNamespace0_CTD_ANON_planet', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 28, 1), )

    
    planet = property(__planet.value, __planet.set, None, None)

    
    # Element star uses Python identifier star
    __star = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'star'), 'star', '__AbsentNamespace0_CTD_ANON_star', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 57, 1), )

    
    star = property(__star.value, __star.set, None, None)

    
    # Element binary uses Python identifier binary
    __binary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'binary'), 'binary', '__AbsentNamespace0_CTD_ANON_binary', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 79, 1), )

    
    binary = property(__binary.value, __binary.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __spectraltype.name() : __spectraltype,
        __rightascension.name() : __rightascension,
        __declination.name() : __declination,
        __distance.name() : __distance,
        __epoch.name() : __epoch,
        __videolink.name() : __videolink,
        __magB.name() : __magB,
        __magV.name() : __magV,
        __magI.name() : __magI,
        __magJ.name() : __magJ,
        __magH.name() : __magH,
        __magK.name() : __magK,
        __magR.name() : __magR,
        __planet.name() : __planet,
        __star.name() : __star,
        __binary.name() : __binary
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_CTD_ANON__name', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 31, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element list uses Python identifier list
    __list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'list'), 'list', '__AbsentNamespace0_CTD_ANON__list', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 32, 4), )

    
    list = property(__list.value, __list.set, None, None)

    
    # Element semimajoraxis uses Python identifier semimajoraxis
    __semimajoraxis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'semimajoraxis'), 'semimajoraxis', '__AbsentNamespace0_CTD_ANON__semimajoraxis', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 33, 4), )

    
    semimajoraxis = property(__semimajoraxis.value, __semimajoraxis.set, None, None)

    
    # Element eccentricity uses Python identifier eccentricity
    __eccentricity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'eccentricity'), 'eccentricity', '__AbsentNamespace0_CTD_ANON__eccentricity', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 34, 4), )

    
    eccentricity = property(__eccentricity.value, __eccentricity.set, None, None)

    
    # Element periastron uses Python identifier periastron
    __periastron = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'periastron'), 'periastron', '__AbsentNamespace0_CTD_ANON__periastron', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 35, 4), )

    
    periastron = property(__periastron.value, __periastron.set, None, None)

    
    # Element longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'longitude'), 'longitude', '__AbsentNamespace0_CTD_ANON__longitude', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 36, 4), )

    
    longitude = property(__longitude.value, __longitude.set, None, None)

    
    # Element ascendingnode uses Python identifier ascendingnode
    __ascendingnode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ascendingnode'), 'ascendingnode', '__AbsentNamespace0_CTD_ANON__ascendingnode', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 37, 4), )

    
    ascendingnode = property(__ascendingnode.value, __ascendingnode.set, None, None)

    
    # Element inclination uses Python identifier inclination
    __inclination = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'inclination'), 'inclination', '__AbsentNamespace0_CTD_ANON__inclination', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 38, 4), )

    
    inclination = property(__inclination.value, __inclination.set, None, None)

    
    # Element period uses Python identifier period
    __period = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'period'), 'period', '__AbsentNamespace0_CTD_ANON__period', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 39, 4), )

    
    period = property(__period.value, __period.set, None, None)

    
    # Element transittime uses Python identifier transittime
    __transittime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'transittime'), 'transittime', '__AbsentNamespace0_CTD_ANON__transittime', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 40, 4), )

    
    transittime = property(__transittime.value, __transittime.set, None, None)

    
    # Element mass uses Python identifier mass
    __mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'mass'), 'mass', '__AbsentNamespace0_CTD_ANON__mass', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 41, 4), )

    
    mass = property(__mass.value, __mass.set, None, None)

    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'radius'), 'radius', '__AbsentNamespace0_CTD_ANON__radius', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 42, 4), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Element temperature uses Python identifier temperature
    __temperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'temperature'), 'temperature', '__AbsentNamespace0_CTD_ANON__temperature', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 43, 4), )

    
    temperature = property(__temperature.value, __temperature.set, None, None)

    
    # Element age uses Python identifier age
    __age = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'age'), 'age', '__AbsentNamespace0_CTD_ANON__age', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 44, 4), )

    
    age = property(__age.value, __age.set, None, None)

    
    # Element discoverymethod uses Python identifier discoverymethod
    __discoverymethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'discoverymethod'), 'discoverymethod', '__AbsentNamespace0_CTD_ANON__discoverymethod', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 45, 4), )

    
    discoverymethod = property(__discoverymethod.value, __discoverymethod.set, None, None)

    
    # Element istransiting uses Python identifier istransiting
    __istransiting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'istransiting'), 'istransiting', '__AbsentNamespace0_CTD_ANON__istransiting', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 46, 4), )

    
    istransiting = property(__istransiting.value, __istransiting.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_CTD_ANON__description', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 47, 4), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element discoveryyear uses Python identifier discoveryyear
    __discoveryyear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'discoveryyear'), 'discoveryyear', '__AbsentNamespace0_CTD_ANON__discoveryyear', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 48, 4), )

    
    discoveryyear = property(__discoveryyear.value, __discoveryyear.set, None, None)

    
    # Element lastupdate uses Python identifier lastupdate
    __lastupdate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'lastupdate'), 'lastupdate', '__AbsentNamespace0_CTD_ANON__lastupdate', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 49, 4), )

    
    lastupdate = property(__lastupdate.value, __lastupdate.set, None, None)

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'image'), 'image', '__AbsentNamespace0_CTD_ANON__image', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 50, 4), )

    
    image = property(__image.value, __image.set, None, None)

    
    # Element imagedescription uses Python identifier imagedescription
    __imagedescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'imagedescription'), 'imagedescription', '__AbsentNamespace0_CTD_ANON__imagedescription', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 51, 4), )

    
    imagedescription = property(__imagedescription.value, __imagedescription.set, None, None)

    
    # Element spinorbitalignment uses Python identifier spinorbitalignment
    __spinorbitalignment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'spinorbitalignment'), 'spinorbitalignment', '__AbsentNamespace0_CTD_ANON__spinorbitalignment', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 52, 4), )

    
    spinorbitalignment = property(__spinorbitalignment.value, __spinorbitalignment.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __list.name() : __list,
        __semimajoraxis.name() : __semimajoraxis,
        __eccentricity.name() : __eccentricity,
        __periastron.name() : __periastron,
        __longitude.name() : __longitude,
        __ascendingnode.name() : __ascendingnode,
        __inclination.name() : __inclination,
        __period.name() : __period,
        __transittime.name() : __transittime,
        __mass.name() : __mass,
        __radius.name() : __radius,
        __temperature.name() : __temperature,
        __age.name() : __age,
        __discoverymethod.name() : __discoverymethod,
        __istransiting.name() : __istransiting,
        __description.name() : __description,
        __discoveryyear.name() : __discoveryyear,
        __lastupdate.name() : __lastupdate,
        __image.name() : __image,
        __imagedescription.name() : __imagedescription,
        __spinorbitalignment.name() : __spinorbitalignment
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 58, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element planet uses Python identifier planet
    __planet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'planet'), 'planet', '__AbsentNamespace0_CTD_ANON_2_planet', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 28, 1), )

    
    planet = property(__planet.value, __planet.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_CTD_ANON_2_name', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 60, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element mass uses Python identifier mass
    __mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'mass'), 'mass', '__AbsentNamespace0_CTD_ANON_2_mass', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 62, 4), )

    
    mass = property(__mass.value, __mass.set, None, None)

    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'radius'), 'radius', '__AbsentNamespace0_CTD_ANON_2_radius', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 63, 4), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Element temperature uses Python identifier temperature
    __temperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'temperature'), 'temperature', '__AbsentNamespace0_CTD_ANON_2_temperature', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 64, 4), )

    
    temperature = property(__temperature.value, __temperature.set, None, None)

    
    # Element age uses Python identifier age
    __age = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'age'), 'age', '__AbsentNamespace0_CTD_ANON_2_age', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 65, 4), )

    
    age = property(__age.value, __age.set, None, None)

    
    # Element metallicity uses Python identifier metallicity
    __metallicity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'metallicity'), 'metallicity', '__AbsentNamespace0_CTD_ANON_2_metallicity', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 66, 4), )

    
    metallicity = property(__metallicity.value, __metallicity.set, None, None)

    
    # Element spectraltype uses Python identifier spectraltype
    __spectraltype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'spectraltype'), 'spectraltype', '__AbsentNamespace0_CTD_ANON_2_spectraltype', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 67, 4), )

    
    spectraltype = property(__spectraltype.value, __spectraltype.set, None, None)

    
    # Element magB uses Python identifier magB
    __magB = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magB'), 'magB', '__AbsentNamespace0_CTD_ANON_2_magB', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 68, 4), )

    
    magB = property(__magB.value, __magB.set, None, None)

    
    # Element magV uses Python identifier magV
    __magV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magV'), 'magV', '__AbsentNamespace0_CTD_ANON_2_magV', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 69, 4), )

    
    magV = property(__magV.value, __magV.set, None, None)

    
    # Element magI uses Python identifier magI
    __magI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magI'), 'magI', '__AbsentNamespace0_CTD_ANON_2_magI', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 70, 4), )

    
    magI = property(__magI.value, __magI.set, None, None)

    
    # Element magJ uses Python identifier magJ
    __magJ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magJ'), 'magJ', '__AbsentNamespace0_CTD_ANON_2_magJ', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 71, 4), )

    
    magJ = property(__magJ.value, __magJ.set, None, None)

    
    # Element magH uses Python identifier magH
    __magH = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magH'), 'magH', '__AbsentNamespace0_CTD_ANON_2_magH', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 72, 4), )

    
    magH = property(__magH.value, __magH.set, None, None)

    
    # Element magK uses Python identifier magK
    __magK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magK'), 'magK', '__AbsentNamespace0_CTD_ANON_2_magK', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 73, 4), )

    
    magK = property(__magK.value, __magK.set, None, None)

    
    # Element magR uses Python identifier magR
    __magR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magR'), 'magR', '__AbsentNamespace0_CTD_ANON_2_magR', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 74, 4), )

    
    magR = property(__magR.value, __magR.set, None, None)

    _ElementMap.update({
        __planet.name() : __planet,
        __name.name() : __name,
        __mass.name() : __mass,
        __radius.name() : __radius,
        __temperature.name() : __temperature,
        __age.name() : __age,
        __metallicity.name() : __metallicity,
        __spectraltype.name() : __spectraltype,
        __magB.name() : __magB,
        __magV.name() : __magV,
        __magI.name() : __magI,
        __magJ.name() : __magJ,
        __magH.name() : __magH,
        __magK.name() : __magK,
        __magR.name() : __magR
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 80, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element planet uses Python identifier planet
    __planet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'planet'), 'planet', '__AbsentNamespace0_CTD_ANON_3_planet', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 28, 1), )

    
    planet = property(__planet.value, __planet.set, None, None)

    
    # Element star uses Python identifier star
    __star = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'star'), 'star', '__AbsentNamespace0_CTD_ANON_3_star', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 57, 1), )

    
    star = property(__star.value, __star.set, None, None)

    
    # Element binary uses Python identifier binary
    __binary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'binary'), 'binary', '__AbsentNamespace0_CTD_ANON_3_binary', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 79, 1), )

    
    binary = property(__binary.value, __binary.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_CTD_ANON_3_name', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 82, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element semimajoraxis uses Python identifier semimajoraxis
    __semimajoraxis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'semimajoraxis'), 'semimajoraxis', '__AbsentNamespace0_CTD_ANON_3_semimajoraxis', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 86, 4), )

    
    semimajoraxis = property(__semimajoraxis.value, __semimajoraxis.set, None, None)

    
    # Element eccentricity uses Python identifier eccentricity
    __eccentricity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'eccentricity'), 'eccentricity', '__AbsentNamespace0_CTD_ANON_3_eccentricity', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 87, 4), )

    
    eccentricity = property(__eccentricity.value, __eccentricity.set, None, None)

    
    # Element periastron uses Python identifier periastron
    __periastron = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'periastron'), 'periastron', '__AbsentNamespace0_CTD_ANON_3_periastron', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 88, 4), )

    
    periastron = property(__periastron.value, __periastron.set, None, None)

    
    # Element longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'longitude'), 'longitude', '__AbsentNamespace0_CTD_ANON_3_longitude', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 89, 4), )

    
    longitude = property(__longitude.value, __longitude.set, None, None)

    
    # Element ascendingnode uses Python identifier ascendingnode
    __ascendingnode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ascendingnode'), 'ascendingnode', '__AbsentNamespace0_CTD_ANON_3_ascendingnode', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 90, 4), )

    
    ascendingnode = property(__ascendingnode.value, __ascendingnode.set, None, None)

    
    # Element inclination uses Python identifier inclination
    __inclination = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'inclination'), 'inclination', '__AbsentNamespace0_CTD_ANON_3_inclination', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 91, 4), )

    
    inclination = property(__inclination.value, __inclination.set, None, None)

    
    # Element period uses Python identifier period
    __period = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'period'), 'period', '__AbsentNamespace0_CTD_ANON_3_period', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 92, 4), )

    
    period = property(__period.value, __period.set, None, None)

    
    # Element transittime uses Python identifier transittime
    __transittime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'transittime'), 'transittime', '__AbsentNamespace0_CTD_ANON_3_transittime', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 93, 4), )

    
    transittime = property(__transittime.value, __transittime.set, None, None)

    
    # Element magB uses Python identifier magB
    __magB = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magB'), 'magB', '__AbsentNamespace0_CTD_ANON_3_magB', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 94, 4), )

    
    magB = property(__magB.value, __magB.set, None, None)

    
    # Element magV uses Python identifier magV
    __magV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magV'), 'magV', '__AbsentNamespace0_CTD_ANON_3_magV', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 95, 4), )

    
    magV = property(__magV.value, __magV.set, None, None)

    
    # Element magI uses Python identifier magI
    __magI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magI'), 'magI', '__AbsentNamespace0_CTD_ANON_3_magI', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 96, 4), )

    
    magI = property(__magI.value, __magI.set, None, None)

    
    # Element magJ uses Python identifier magJ
    __magJ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magJ'), 'magJ', '__AbsentNamespace0_CTD_ANON_3_magJ', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 97, 4), )

    
    magJ = property(__magJ.value, __magJ.set, None, None)

    
    # Element magH uses Python identifier magH
    __magH = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magH'), 'magH', '__AbsentNamespace0_CTD_ANON_3_magH', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 98, 4), )

    
    magH = property(__magH.value, __magH.set, None, None)

    
    # Element magK uses Python identifier magK
    __magK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magK'), 'magK', '__AbsentNamespace0_CTD_ANON_3_magK', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 99, 4), )

    
    magK = property(__magK.value, __magK.set, None, None)

    
    # Element magR uses Python identifier magR
    __magR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'magR'), 'magR', '__AbsentNamespace0_CTD_ANON_3_magR', True, pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 100, 4), )

    
    magR = property(__magR.value, __magR.set, None, None)

    _ElementMap.update({
        __planet.name() : __planet,
        __star.name() : __star,
        __binary.name() : __binary,
        __name.name() : __name,
        __semimajoraxis.name() : __semimajoraxis,
        __eccentricity.name() : __eccentricity,
        __periastron.name() : __periastron,
        __longitude.name() : __longitude,
        __ascendingnode.name() : __ascendingnode,
        __inclination.name() : __inclination,
        __period.name() : __period,
        __transittime.name() : __transittime,
        __magB.name() : __magB,
        __magV.name() : __magV,
        __magI.name() : __magI,
        __magJ.name() : __magJ,
        __magH.name() : __magH,
        __magK.name() : __magK,
        __magR.name() : __magR
    })
    _AttributeMap.update({
        
    })



# Complex type number with content type SIMPLE
class number (pyxb.binding.basis.complexTypeDefinition):
    """Complex type number with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'number')
    _XSDLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 115, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute errorminus uses Python identifier errorminus
    __errorminus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'errorminus'), 'errorminus', '__AbsentNamespace0_number_errorminus', pyxb.binding.datatypes.double)
    __errorminus._DeclarationLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 118, 4)
    __errorminus._UseLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 118, 4)
    
    errorminus = property(__errorminus.value, __errorminus.set, None, None)

    
    # Attribute errorplus uses Python identifier errorplus
    __errorplus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'errorplus'), 'errorplus', '__AbsentNamespace0_number_errorplus', pyxb.binding.datatypes.double)
    __errorplus._DeclarationLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 119, 4)
    __errorplus._UseLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 119, 4)
    
    errorplus = property(__errorplus.value, __errorplus.set, None, None)

    
    # Attribute lowerlimit uses Python identifier lowerlimit
    __lowerlimit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lowerlimit'), 'lowerlimit', '__AbsentNamespace0_number_lowerlimit', pyxb.binding.datatypes.double)
    __lowerlimit._DeclarationLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 120, 4)
    __lowerlimit._UseLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 120, 4)
    
    lowerlimit = property(__lowerlimit.value, __lowerlimit.set, None, None)

    
    # Attribute upperlimit uses Python identifier upperlimit
    __upperlimit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'upperlimit'), 'upperlimit', '__AbsentNamespace0_number_upperlimit', pyxb.binding.datatypes.double)
    __upperlimit._DeclarationLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 121, 4)
    __upperlimit._UseLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 121, 4)
    
    upperlimit = property(__upperlimit.value, __upperlimit.set, None, None)

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__AbsentNamespace0_number_unit', pyxb.binding.datatypes.string)
    __unit._DeclarationLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 122, 4)
    __unit._UseLocation = pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 122, 4)
    
    unit = property(__unit.value, __unit.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __errorminus.name() : __errorminus,
        __errorplus.name() : __errorplus,
        __lowerlimit.name() : __lowerlimit,
        __upperlimit.name() : __upperlimit,
        __unit.name() : __unit
    })
Namespace.addCategoryObject('typeBinding', u'number', number)


system = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'system'), CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 4, 1))
Namespace.addCategoryObject('elementBinding', system.name().localName(), system)

planet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planet'), CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', planet.name().localName(), planet)

star = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'star'), CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 57, 1))
Namespace.addCategoryObject('elementBinding', star.name().localName(), star)

binary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'binary'), CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 79, 1))
Namespace.addCategoryObject('elementBinding', binary.name().localName(), binary)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 7, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'spectraltype'), spectraltypedef, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 11, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'rightascension'), rightascensiondef, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 12, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'declination'), declinationdef, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 13, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'distance'), number, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 14, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'epoch'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 15, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'videolink'), webreference, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 16, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magB'), number, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 17, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magV'), number, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 18, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magI'), number, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 19, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magJ'), number, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 20, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magH'), number, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 21, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magK'), number, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 22, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magR'), number, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 23, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planet'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 28, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'star'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 57, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'binary'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 79, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 8, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 9, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 11, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 14, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 15, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 16, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 17, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 18, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 19, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 20, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 21, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 22, 4))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 23, 4))
    counters.add(cc_12)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 7, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'binary')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 8, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'planet')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 9, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'star')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 10, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'spectraltype')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 11, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'rightascension')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 12, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'declination')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 13, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'distance')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 14, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'epoch')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 15, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'videolink')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 16, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'magB')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 17, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'magV')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 18, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'magI')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 19, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'magJ')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 20, 4))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'magH')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 21, 4))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'magK')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 22, 4))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'magR')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 23, 4))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 31, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'list'), listtype, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 32, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'semimajoraxis'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 33, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'eccentricity'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 34, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'periastron'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 35, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'longitude'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 36, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ascendingnode'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 37, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'inclination'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 38, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'period'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 39, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'transittime'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 40, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'mass'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 41, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'radius'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 42, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'temperature'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 43, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'age'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 44, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'discoverymethod'), discoverymethodtype, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 45, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'istransiting'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 46, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 47, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'discoveryyear'), year, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 48, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'lastupdate'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 49, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'image'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 50, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'imagedescription'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 51, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'spinorbitalignment'), number, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 52, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 32, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 33, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 34, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 35, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 36, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 37, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 38, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 39, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 40, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 41, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 42, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 43, 4))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 44, 4))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 45, 4))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 46, 4))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 47, 4))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 48, 4))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 49, 4))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 50, 4))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 51, 4))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 52, 4))
    counters.add(cc_20)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 31, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'list')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 32, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'semimajoraxis')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 33, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'eccentricity')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 34, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'periastron')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 35, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'longitude')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 36, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'ascendingnode')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 37, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'inclination')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 38, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'period')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 39, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'transittime')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 40, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'mass')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 41, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'radius')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 42, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'temperature')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 43, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'age')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 44, 4))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'discoverymethod')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 45, 4))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'istransiting')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 46, 4))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 47, 4))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'discoveryyear')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 48, 4))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'lastupdate')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 49, 4))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'image')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 50, 4))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'imagedescription')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 51, 4))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'spinorbitalignment')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 52, 4))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_21._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planet'), CTD_ANON_, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 28, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 60, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'mass'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 62, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'radius'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 63, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'temperature'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 64, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'age'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 65, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'metallicity'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 66, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'spectraltype'), spectraltypedef, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 67, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magB'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 68, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magV'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 69, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magI'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 70, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magJ'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 71, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magH'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 72, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magK'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 73, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magR'), number, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 74, 4)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 61, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 62, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 63, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 65, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 66, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 67, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 68, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 69, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 70, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 71, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 72, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 73, 4))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 74, 4))
    counters.add(cc_12)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 60, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'planet')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 61, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'mass')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 62, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'radius')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 63, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'temperature')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 64, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'age')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 65, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'metallicity')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 66, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'spectraltype')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 67, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'magB')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 68, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'magV')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 69, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'magI')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 70, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'magJ')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 71, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'magH')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 72, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'magK')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 73, 4))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'magR')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 74, 4))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planet'), CTD_ANON_, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 28, 1)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'star'), CTD_ANON_2, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 57, 1)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'binary'), CTD_ANON_3, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 79, 1)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 82, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'semimajoraxis'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 86, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'eccentricity'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 87, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'periastron'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 88, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'longitude'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 89, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ascendingnode'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 90, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'inclination'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 91, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'period'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 92, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'transittime'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 93, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magB'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 94, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magV'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 95, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magI'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 96, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magJ'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 97, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magH'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 98, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magK'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 99, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'magR'), number, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 100, 4)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 83, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 84, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 94, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 95, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 96, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 97, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 98, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 99, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 100, 4))
    counters.add(cc_8)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 82, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'binary')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 83, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'star')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 84, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'planet')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 85, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'semimajoraxis')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 86, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'eccentricity')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 87, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'periastron')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 88, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'longitude')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 89, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'ascendingnode')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 90, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'inclination')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 91, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'period')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 92, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'transittime')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 93, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'magB')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 94, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'magV')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 95, 4))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'magI')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 96, 4))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'magJ')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 97, 4))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'magH')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 98, 4))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'magK')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 99, 4))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'magR')), pyxb.utils.utility.Location('/home/caden/school/open_exo/catalog_workspace/open_exoplanet_catalogue/oec.xsd', 100, 4))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()

