"""
Stage 8: Unit Testing
=====================
Concepts: pytest, unit testing, test fixtures, assertions

To test your work:
    uv run pytest stages/stage8_tests.py -v

Your Task:
----------
Write comprehensive unit tests for the functions you implemented in previous stages.

Learning Objectives:
- Write unit tests using pytest
- Use test fixtures for shared setup
- Test edge cases and error conditions
- Use assertions effectively
- Understand test coverage
"""

import pytest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from stages.stage1_parsing import parse_ingredients
from stages.stage2_ingredient import Ingredient, create_unknown_ingredient
from stages.stage3_database import IngredientDatabase
from stages.stage5_scoring import calculate_overall_score, get_score_label, count_by_category


class TestStage1Parsing:
    """Tests for Stage 1: Ingredient Parsing"""

    def test_basic_parsing(self):
        """Test basic comma-separated parsing."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Test that parse_ingredients("Water, Sugar, Salt") returns
        # ['water', 'sugar', 'salt']
        #
        # Use: assert result == expected
        #
        # Delete the line below and write your test:
        pass
        # ============================================================

    def test_whitespace_handling(self):
        """Test that extra whitespace is handled correctly."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Test that "  Flour  ,  SUGAR,salt  " returns ['flour', 'sugar', 'salt']
        #
        # Delete the line below and write your test:
        pass
        # ============================================================

    def test_empty_string(self):
        """Test that empty string returns empty list."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Test that parse_ingredients("") returns []
        #
        # Delete the line below and write your test:
        pass
        # ============================================================

    def test_parenthetical_removal(self):
        """Test that parenthetical content is removed."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Test that "Red 40 (for color), Sugar" returns ['red 40', 'sugar']
        #
        # Delete the line below and write your test:
        pass
        # ============================================================

    def test_single_ingredient(self):
        """Test single ingredient without commas."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Test that "Water" returns ['water']
        #
        # Delete the line below and write your test:
        pass
        # ============================================================


class TestStage2Ingredient:
    """Tests for Stage 2: Ingredient Dataclass"""

    def test_ingredient_creation_minimal(self):
        """Test creating an Ingredient with just the name."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Create an Ingredient with only name="sugar"
        # Check that default values are set correctly:
        # - category should be "unknown"
        # - health_score should be 5
        # - found_in_database should be False
        #
        # Delete the lines below and write your test:
        pass
        # ============================================================

    def test_ingredient_creation_full(self):
        """Test creating an Ingredient with all fields."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Create an Ingredient with all fields specified
        # Verify each field has the expected value
        #
        # Delete the lines below and write your test:
        pass
        # ============================================================

    def test_create_unknown_ingredient(self):
        """Test the create_unknown_ingredient factory function."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Test that create_unknown_ingredient("mystery") returns
        # an Ingredient with:
        # - name="mystery"
        # - category="unknown"
        # - found_in_database=False
        #
        # Delete the lines below and write your test:
        pass
        # ============================================================


class TestStage3Database:
    """Tests for Stage 3: Ingredient Database"""

    @pytest.fixture
    def database(self):
        """Fixture to provide a loaded database for tests."""
        db_path = Path(__file__).parent.parent / "data" / "ingredients_db.json"
        return IngredientDatabase(str(db_path))

    def test_database_loads(self, database):
        """Test that the database loads successfully."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Check that len(database) > 0
        #
        # Delete the line below and write your test:
        pass
        # ============================================================

    def test_lookup_existing_ingredient(self, database):
        """Test looking up an ingredient that exists."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Look up "sugar" and verify:
        # - Result is not None
        # - Result has 'category' key
        # - Result has 'health_score' key
        #
        # Delete the lines below and write your test:
        pass
        # ============================================================

    def test_lookup_case_insensitive(self, database):
        """Test that lookup is case-insensitive."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Verify that database.lookup("SUGAR") returns the same as
        # database.lookup("sugar")
        #
        # Delete the lines below and write your test:
        pass
        # ============================================================

    def test_lookup_nonexistent(self, database):
        """Test looking up an ingredient that doesn't exist."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Verify that database.lookup("unicorn tears") returns None
        #
        # Delete the line below and write your test:
        pass
        # ============================================================

    def test_contains_operator(self, database):
        """Test the 'in' operator with the database."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Verify:
        # - "water" in database is True
        # - "unicorn tears" in database is False
        #
        # Delete the lines below and write your test:
        pass
        # ============================================================


class TestStage5Scoring:
    """Tests for Stage 5: Health Scoring"""

    @pytest.fixture
    def sample_ingredients(self):
        """Fixture providing sample ingredients for testing."""
        return [
            Ingredient(name="water", category="healthy", health_score=10,
                      description="Good", found_in_database=True),
            Ingredient(name="sugar", category="harmful", health_score=2,
                      description="Bad", found_in_database=True),
        ]

    def test_calculate_score_empty_list(self):
        """Test score calculation with empty list returns 5.0."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Verify calculate_overall_score([]) returns 5.0
        #
        # Delete the line below and write your test:
        pass
        # ============================================================

    def test_calculate_score_basic(self, sample_ingredients):
        """Test basic score calculation."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Calculate score for sample_ingredients
        # Expected: (10 + 2) / 2 = 6.0 (both have weight 1.0)
        #
        # Delete the line below and write your test:
        pass
        # ============================================================

    def test_score_label_excellent(self):
        """Test that scores 8-10 return 'Excellent'."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Test get_score_label(8.0), get_score_label(9.0), get_score_label(10.0)
        # all return "Excellent"
        #
        # Delete the lines below and write your test:
        pass
        # ============================================================

    def test_score_label_poor(self):
        """Test that scores 0-3.9 return 'Poor'."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Test get_score_label(0.0), get_score_label(2.0), get_score_label(3.9)
        # all return "Poor"
        #
        # Delete the lines below and write your test:
        pass
        # ============================================================

    def test_count_by_category(self, sample_ingredients):
        """Test counting ingredients by category."""
        # ============================================================
        # TODO: YOUR CODE HERE
        # ============================================================
        # Verify count_by_category returns {'healthy': 1, 'harmful': 1}
        #
        # Delete the line below and write your test:
        pass
        # ============================================================


def is_implemented() -> bool:
    """Check if this stage is implemented by running a subset of tests."""
    import inspect
    source = inspect.getsource(TestStage1Parsing.test_basic_parsing)
    return "assert" in source and "pass" not in source.split("assert")[0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
