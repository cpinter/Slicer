/*==============================================================================

  Program: 3D Slicer

  Copyright (c) Laboratory for Percutaneous Surgery (PerkLab)
  Queen's University, Kingston, ON, Canada. All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Csaba Pinter, PerkLab, Queen's University
  and was supported through the Applied Cancer Research Unit program of Cancer Care
  Ontario with funds provided by the Ontario Ministry of Health and Long-Term Care

==============================================================================*/

#ifndef __qSlicerColorTableTerminologyDelegate_h
#define __qSlicerColorTableTerminologyDelegate_h

// Qt includes
#include <QStyledItemDelegate>
#include <QModelIndex>

#include "qSlicerColorsModuleWidgetsExport.h"

// \brief Delegate for displaying terminology selector
class Q_SLICER_MODULE_COLORS_WIDGETS_EXPORT qSlicerColorTableTerminologyDelegate : public QStyledItemDelegate
{
  Q_OBJECT

public:
  qSlicerColorTableTerminologyDelegate(QObject *parent = nullptr);

  QWidget* createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const override;

  void setEditorData(QWidget *editor, const QModelIndex &index) const override;
  void setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const override;

  void updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const override;

protected slots:
  void commitSenderData();
  void commitAndClose();
  void close();
};

#endif
