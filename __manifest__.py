# -*- coding: utf-8 -*-
{
    'name': "coba_module",

    'summary': """
        Modul ini bakal jadi percobaan
        """,

    'description': """
        Academic Information System Day 1
    """,

    'depends': [
        'base',
        'account',
        'sale',
        'board',
    ],

    'author': "Kudit",
    'website': "http://github.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Belajar',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'menu.xml',
        'views/views_course.xml',
        'views/views_session.xml',
        'views/views_attendee.xml',
        'views/views_partner.xml',
        'views/templates.xml',
        'views/workflow.xml',
        'security/group.xml',
        'security/ir.model.access.csv',
        'wizard/create_attendee_view.xml',
        'report/session_report.xml',
        'dashboard.xml'
        
    ],

    'installable': True,
    'auto-install': False,
    'application': True,
    
    
}