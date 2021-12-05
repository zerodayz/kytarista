# kytarista
Programming guitar music

## Requirements

### MacOS

```bash
brew install ffmpeg
```

### Linux

```bash
apt-get install ffmpeg libavcodec-extra
```

## Import Guitar package

```python
from kytarista import Guitar
```

## Initialize the Guitar

```python
guitar = Guitar('slg200s', 'acoustic')
guitar.initialize()
```

## Play C major chord
```python
guitar.play('c')
```

## Play sequence of chords
```python
guitar.sequence('c d e f#')
```