-- Colour comparison marks: ✓ green, ✗ red, ◐ amber (standalone tokens only).
local cls = { ["✓"] = "ok", ["✗"] = "no", ["◐"] = "part" }
function Str(el)
  local c = cls[el.text]
  if c then return pandoc.Span(el.text, { class = c }) end
end
