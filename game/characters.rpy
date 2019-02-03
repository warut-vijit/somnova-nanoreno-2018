# what_prefix = "“", what_suffix = "”"
# That bit of code makes the character's speech be preceded and followed by quotation marks. This
# is for convenience, so we don't have to do this ourselves for every line of dialogue we write. 

define debug = Character("Debug", who_color = "#ff00ff")

##########################################
##----------PRIMARY CHARACTERS----------##
##########################################

define eris = Character("Eris", what_prefix = "“", what_suffix = "”", image = "eris", who_color = "#59ff9b", ctc="ctctyping", ctc_position="nestled")
define roman = Character("Roman", what_prefix = "“", what_suffix = "”", who_color = "#b37664", ctc="ctctyping", ctc_position="nestled")
define parker = Character("Parker", what_prefix = "“", what_suffix = "”", image = "parker", who_color = "#f1c564", ctc="ctctyping", ctc_position="nestled")

##########################################
##--------INCIDENTAL CHARACTERS---------##
##########################################

define customer_a = Character("Customer A", what_prefix = "“", what_suffix = "”", ctc="ctctyping", ctc_position="nestled")
define customer_b = Character("Customer B", what_prefix = "“", what_suffix = "”", ctc="ctctyping", ctc_position="nestled")
define navcomp = Character("Navcomp", what_prefix = "“", what_suffix = "”", ctc="ctctyping", ctc_position="nestled")
define phone = Character("Phone", what_prefix = "“", what_suffix = "”", ctc="ctctyping", ctc_position="nestled")

##########################################
##----------UTILITY CHARACTERS----------##
##########################################

# For use before Roman recognizes Eris.
define waitress_girl = Character("Waitress Girl", what_prefix = "”", what_suffix = "”", ctc="ctctyping", ctc_position="nestled")