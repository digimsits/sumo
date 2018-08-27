#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot)

# recompute
netedit.rebuildNetwork()

# go to inspect mode
netedit.inspectMode()

# inspect edge
netedit.leftClick(match, 250, 180)

# Change parameter 10 with an non valid value
netedit.modifyAttribute(10, "DummyDisallowed")

# Change parameter 10 with a valid value (empty)
netedit.modifyAttribute(10, "")

# Change parameter 10 with a valid value (different separators)
netedit.modifyAttribute(10, "authority  army, passenger; taxi. tram")

# Change parameter 10 with a valid value (empty)
netedit.modifyAttribute(10, "")

# Change parameter 10 with a valid value (empty)
netedit.modifyAttribute(
    10, "emergency authority army vip passenger hov bus coach tram rail_urban rail " +
    "rail_electric motorcycle moped pedestrian custom1")

# recompute
netedit.rebuildNetwork()

# Check undos
netedit.undo(match, 1)

# recompute
netedit.rebuildNetwork()

# check redos
netedit.redo(match, 1)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
