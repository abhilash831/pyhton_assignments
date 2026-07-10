from src.text_alignment.util import generate_logo

def test_generate_logo_thickness_five():
    logo = generate_logo(5)
    lines = logo.split("\n")
    
    assert len(lines) == 25
    assert lines[0].strip() == "H"
    assert lines[4].strip() == "HHHHHHHHH"
    assert lines[-1].strip() == "H"

def test_generate_logo_thickness_three():
    logo = generate_logo(3)
    lines = logo.split("\n")
    
    assert len(lines) == 15
    assert lines[0].strip() == "H"
    assert lines[-1].strip() == "H"