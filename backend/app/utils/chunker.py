import re


def chunk_text(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 100,
) -> list[str]:
    """Split text into chunks respecting paragraph and sentence boundaries."""
    paragraphs = re.split(r"\n\s*\n", text.strip())

    chunks: list[str] = []
    current_chunk = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # If adding this paragraph stays within chunk_size, append it
        candidate = f"{current_chunk}\n\n{para}".strip() if current_chunk else para
        if len(candidate) <= chunk_size:
            current_chunk = candidate
        else:
            # Save current chunk if non-empty
            if current_chunk:
                chunks.append(current_chunk)

            # If the paragraph itself is too big, split by sentences
            if len(para) > chunk_size:
                sentences = re.split(r"(?<=[.!?])\s+", para)
                current_chunk = ""
                for sentence in sentences:
                    candidate = (
                        f"{current_chunk} {sentence}".strip()
                        if current_chunk
                        else sentence
                    )
                    if len(candidate) <= chunk_size:
                        current_chunk = candidate
                    else:
                        if current_chunk:
                            chunks.append(current_chunk)
                        current_chunk = sentence
            else:
                current_chunk = para

    if current_chunk:
        chunks.append(current_chunk)

    # Apply overlap: prepend tail of previous chunk to next chunk
    if chunk_overlap > 0 and len(chunks) > 1:
        overlapped = [chunks[0]]
        for i in range(1, len(chunks)):
            prev_tail = chunks[i - 1][-chunk_overlap:]
            # Find a word boundary for cleaner overlap
            space_idx = prev_tail.find(" ")
            if space_idx != -1:
                prev_tail = prev_tail[space_idx + 1 :]
            overlapped.append(f"{prev_tail}\n\n{chunks[i]}")
        chunks = overlapped

    return chunks
