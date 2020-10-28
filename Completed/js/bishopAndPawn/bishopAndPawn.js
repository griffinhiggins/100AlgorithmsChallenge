function bishopAndPawn(b, p) {
  return (
    Math.abs(b.charCodeAt(0) - p.charCodeAt(0)) ==
    Math.abs(parseInt(b[1]) - parseInt(p[1]))
  );
}
console.log(bishopAndPawn('a1', 'c3'));
