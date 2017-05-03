import unittest

import sphinx

from readthedocs_ext.readthedocs import HtmlBuilderMixin

from .util import sphinx_build


class MixinTests(unittest.TestCase):

    def test_html_builder_context_contains_overrides(self):
        with sphinx_build('pyexample', 'readthedocs') as app:
            self.assertIn(
                'search_scorer_tool',
                app.builder.get_static_override_context(),
            )

    def test_htmldir_builder_context_contains_overrides(self):
        with sphinx_build('pyexample', 'readthedocsdirhtml') as app:
            self.assertIn(
                'search_scorer_tool',
                app.builder.get_static_override_context(),
            )

    def test_comments_builder_context_contains_overrides(self):
        with sphinx_build('pyexample', 'readthedocs-comments') as app:
            self.assertIn(
                'websupport2_base_url',
                app.builder.get_static_override_context(),
            )
