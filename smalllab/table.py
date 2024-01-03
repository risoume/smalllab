"""This module contains functions for generating html table.
"""

def table_h(H: list, *L: list) -> str:
    """Return html table with heading H and rows *L = L1, l2, ..., Ln.
    If there is no heading, enter empty list as the first argument.
    """
    list_count = len(L)
    elem_count = len(L[0])
    
    s = "<table>"
    for j in range(list_count):
        s += "<tr>"
        if H:
            s += "<th>" + str( H[j] ) + "</th>"
        for k in range(elem_count):
            s += "<td>" + str( L[j][k] ) + "</td>"
        s += "</tr>"
        
    s += "</table>"
    return s


def table_h2(H: list, *L: list) -> str:
    """Return html table with heading H and rows *L = L1, l2, ..., Ln.
    If there is no heading, enter empty list as the first argument.
    The heading is displayed as row.
    """
    list_count = len(L)
    elem_count = len(L[0])
    
    s = "<table>"
    if H:
        s += "<tr>"
        for h in H:
            s += "<th>" + str( h ) + "</th>"
        s += "</tr>"
    
    for j in range(list_count):
        s += "<tr>"
        for k in range(elem_count):
            s += "<td>" + str( L[j][k] ) + "</td>"
        s += "</tr>"
        
    s += "</table>"
    return s


def table_h_tex(H: list, *L: list) -> str:
    """Return html table with heading H and rows *L = L1, l2, ..., Ln.
    If there is no heading, enter empty list as the first argument.
    All entries are displayed in LaTeX.
    """
    list_count = len(L)
    elem_count = len(L[0])
    
    s = "<table>"
    for j in range(list_count):
        s += "<tr>"
        if H:
            s += "<th>" + str( H[j] ) + "</th>"
        for k in range(elem_count):
            s += "<td>$" + str( L[j][k] ) + "$</td>"
        s += "</tr>"
        
    s += "</table>"
    return s


def table_h2_tex(H: list, *L: list) -> str:
    """Return html table with heading H and rows *L = L1, l2, ..., Ln.
    If there is no heading, enter empty list as the first argument.
    The heading is displayed as row.
    All entries are displayed in LaTeX.
    """
    list_count = len(L)
    elem_count = len(L[0])
    
    s = "<table>"
    if H:
        s += "<tr>"
        for h in H:
            s += "<th>" + str( h ) + "</th>"
        s += "</tr>"
    
    for j in range(list_count):
        s += "<tr>"
        for k in range(elem_count):
            s += "<td>$" + str( L[j][k] ) + "$</td>"
        s += "</tr>"
        
    s += "</table>"
    return s


def table_v(H: list, *L: list) -> str:
    """Return html table with heading H and columns *L = L1, l2, ..., Ln.
    If there is no heading, enter empty list as the first argument.
    """
    list_count = len(L)
    elem_count = len(L[0])
    
    s = "<table>"
    if H:
        s += "<tr>"
        for h in H:
            s += "<th>" + str( h ) + "</th>"
        s += "</tr>"
    
    for j in range(elem_count):
        s += "<tr>"
        for k in range(list_count):
            s += "<td>" + str( L[k][j] ) + "</td>"
        s += "</tr>"  
        
    s += "</table>"
    return s


def table_v2(H: list, *L: list) -> str:
    """Return html table with heading H and columns *L = L1, l2, ..., Ln.
    If there is no heading, enter empty list as the first argument.
    The heading is displayed as column.
    """
    list_count = len(L)
    elem_count = len(L[0])
    
    s = "<table>"
    
    for j in range(elem_count):
        s += "<tr>"
        if H:
            s += "<th>" + str( H[j] ) + "</th>"
        for k in range(list_count):
            s += "<td>" + str( L[k][j] ) + "</td>"
        s += "</tr>"  
        
    s += "</table>"
    return s


def table_v_tex(H: list, *L: list) -> str:
    """Return html table with heading H and columns *L = L1, l2, ..., Ln.
    If there is no heading, enter empty list as the first argument.
    All entries are displayed in LaTeX.
    """
    list_count = len(L)
    elem_count = len(L[0])
    
    s = "<table>"
    if H:
        s += "<tr>"
        for h in H:
            s += "<th>" + str( h ) + "</th>"
        s += "</tr>"
    
    for j in range(elem_count):
        s += "<tr>"
        for k in range(list_count):
            s += "<td>$" + str( L[k][j] ) + "$</td>"
        s += "</tr>"  
        
    s += "</table>"
    return s


def table_v2_tex(H: list, *L: list) -> str:
    """Return html table with heading H and columns *L = L1, l2, ..., Ln.
    If there is no heading, enter empty list as the first argument.
    The heading is displayed as column.
    All entries are displayed in LaTeX.
    """
    list_count = len(L)
    elem_count = len(L[0])
    
    s = "<table>"
    
    for j in range(elem_count):
        s += "<tr>"
        if H:
            s += "<th>" + str( H[j] ) + "</th>"
        for k in range(list_count):
            s += "<td>$" + str( L[k][j] ) + "$</td>"
        s += "</tr>"  
        
    s += "</table>"
    return s


def list2table(L: list, n: int) -> str:
    """Convert a list into html table where each row contains n entries."""
    L_ = L[:]
    elem_count = len(L_)
    rows = 1
    if elem_count % n == 0:
        rows = elem_count // n
    else:
        rows = (elem_count // n) + 1
        L_ += ['' for i in range(n - (elem_count % n))]

    s = "<table>"
    for r in range(rows):
        s += "<tr>"
        for i in range(n):
            s += "<td>" + str( L_[r*n+i] ) + "</td>"
        s += "</tr>"
    
    s += "</table>"
    return s

