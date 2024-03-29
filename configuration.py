#!/usr/bin/env python

"""Contains extractor configuration information
"""

# Setup the name of our extractor.
EXTRACTOR_NAME = "Test-CanopyCover"

# Name of scientific method for this extractor. Leave commented out if it's unknown
#METHOD_NAME = ""

# The version number of the extractor
VERSION = "1.0"

# The extractor description
DESCRIPTION = "Testing plot extractor template"

# The name of the author of the extractor
AUTHOR_NAME = "Chris Schnaufer"

# The email of the author of the extractor
AUTHOR_EMAIL = "schnaufer@email.arizona.edu"

# Reposity URI
REPOSITORY = "https://github.com/Chris-Schnaufer/plot-extractor-test.git"

# Output variable identifiers. Use a comma separated list if more than one value is returned.
# For example, "variable 1,variable 2" identifies the two variables returned by the extractor.
# If only one name is specified, no comma's are used.
# Note that variable names cannot have comma's in them: use a different separator instead. Also,
# all white space is kept intact; don't add any extra whitespace since it may cause name comparisons
# to fail
VARIABLE_NAMES = "canopy_cover"
