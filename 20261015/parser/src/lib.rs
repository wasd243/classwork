use pyo3::prelude::*;

#[pyclass]
#[derive(Debug, PartialEq)]
pub struct Recommend {
    pub lang: String,
    pub years: u8,
    pub study_per_week: f32,
}

#[pymethods]
impl Recommend {
    #[new]
    pub fn new(lang: String, years: u8, study_per_week: f32) -> Self {
        Self { lang, years, study_per_week }
    }

    pub fn recommend(&self) -> String {
        let direction = match (self.lang.as_str(), self.years, self.study_per_week) {
            ("Rust", 1.., _) => "Compiler development",
            ("Python", _, _) => "Programming fundamentals",
            (_, 0, _) => "Learn programming basics",
            _ => "Software development",
        };

        format!("Recommended direction: {direction}")
    }
}

#[pymodule]
mod parser {
    #[pymodule_export]
    use super::Recommend;
}
