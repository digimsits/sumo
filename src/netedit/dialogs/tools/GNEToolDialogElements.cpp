/****************************************************************************/
// Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
// Copyright (C) 2001-2022 German Aerospace Center (DLR) and others.
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// https://www.eclipse.org/legal/epl-2.0/
// This Source Code may also be made available under the following Secondary
// Licenses when the conditions for such availability set forth in the Eclipse
// Public License 2.0 are satisfied: GNU General Public License, version 2
// or later which is available at
// https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
// SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later
/****************************************************************************/
/// @file    GNEToolDialog.cpp
/// @author  Pablo Alvarez Lopez
/// @date    Jun 2022
///
// Elements used in GNEToolDialog
/****************************************************************************/
#include <config.h>

#include "GNEToolDialog.h"
#include "GNEToolDialogElements.h"



// ============================================-===============================
// member method definitions
// ===========================================================================

GNEToolDialogElements::Argument::Argument(const std::string name, const std::string parameter_) :
    argumentName(name),
    parameter(parameter_) {
}


GNEToolDialogElements::Argument::~Argument() {}


GNEToolDialogElements::Argument::Argument() {}


GNEToolDialogElements::FileNameArgument::FileNameArgument(FXComposite *parent, const std::string name, const std::string parameter) :
    FXHorizontalFrame(parent),
    Argument(name, parameter){
}

std::string 
GNEToolDialogElements::FileNameArgument::getArgument() const {
    return "";
}

/****************************************************************************/
