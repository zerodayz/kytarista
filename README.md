# kytarista
Programming guitar music


## Import Guitar package

```python
from guitar import Guitar
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