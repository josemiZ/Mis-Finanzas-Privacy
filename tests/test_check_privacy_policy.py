import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('checker', ROOT / 'scripts/check_privacy_policy.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PolicyTests(unittest.TestCase):
    def setUp(self):
        self.html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.policy = checker.Policy(self.html)

    def test_equal_with_entities_and_whitespace(self):
        changed = self.html.replace('Sin cuenta', 'Sin&#32;cuenta').replace('Mis Finanzas es', 'Mis  Finanzas\nes')
        self.assertEqual([], checker.compare(self.policy, checker.Policy(changed)))

    def test_detect_text_summary_and_revision(self):
        for old, new, label in [('Mis Finanzas es desarrollada', 'La app es desarrollada', 'sección 1'),
                                ('Mis Finanzas funciona', 'La app funciona', 'summary'),
                                ('26 de septiembre de 2026', '27 de septiembre de 2026', 'updated'),
                                ('datetime="2026-09-26"', 'datetime="2026-09-25"', 'atributo datetime del sitio')]:
            with self.subTest(label=label):
                self.assertIn(label, checker.compare(self.policy, checker.Policy(self.html.replace(old, new))))

    def test_reject_missing_or_reordered_sections(self):
        for changed in [self.html.replace('<section id="responsable">', '<div>').replace('</section>', '</div>', 1),
                        self.html.replace('>01</span>', '>02</span>')]:
            with self.assertRaises(ValueError):
                checker.Policy(changed)


if __name__ == '__main__':
    unittest.main()
