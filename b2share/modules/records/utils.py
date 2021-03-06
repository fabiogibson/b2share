# -*- coding: utf-8 -*-
#
# This file is part of EUDAT B2Share.
# Copyright (C) 2016 CERN.
#
# B2Share is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# B2Share is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with B2Share; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Record utils."""

from invenio_records.models import RecordMetadata
from invenio_records_files.api import Record


def is_publication(record):
    """Check if a given record is a published record.

    Returns:
        bool: True if the record is a published record, else False.
    """
    return record.json['$schema'].endswith('#/json_schema')


def is_deposit(record):
    """Check if a given record is a deposit record.

    Returns:
        bool: True if the record is a deposit record, else False.
    """
    return record.json['$schema'].endswith('#/draft_json_schema')




def list_db_published_records():
    """A generator for all the published records"""
    query = RecordMetadata.query.filter(RecordMetadata.json != None)
    for obj in query.all():
        record = Record(obj.json, model=obj)
        if is_publication(record.model):
            yield record
