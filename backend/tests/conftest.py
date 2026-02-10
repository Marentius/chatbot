import pytest


@pytest.fixture
def sample_chunks():
    return [
        {
            "text": "Vetle Marentius Nilsen er en fullstack-utvikler med 2 års erfaring, ansatt i Visma SmartSkill AS.",
            "source": "index.md",
            "distance": 0.15,
        },
        {
            "text": "Vetle har erfaring med React, Next.js, TypeScript, Java, Spring Boot, Node.js, Docker og Azure.",
            "source": "index.md",
            "distance": 0.20,
        },
    ]
