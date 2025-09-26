
---

## Alpha-Beta Pruning

An optimization of **Minimax** to reduce unnecessary exploration.

### Key Concepts
- **Alpha (α)** → Best value MAX can guarantee so far.  
- **Beta (β)** → Best value MIN can guarantee so far.  
- **Pruning Rule**: If at any point `α ≥ β`, stop exploring that branch.

### Complexity
- **Worst case**: `O(b^d)` (same as Minimax).  
- **Best case**: `O(b^(d/2))` (dramatic improvement).  

### Process
- Traverse game tree like Minimax.
- Maintain α (max bound) and β (min bound).
- Skip branches that cannot affect the final decision.

**Result**:  
- Same decision as Minimax, but with **fewer evaluations**.  
- Much faster in practice for deep game trees.

---

## Applications

- **Classic Games**:
- Chess, Tic-Tac-Toe, Checkers.
- **Video Games (NPC AI)**:
- Strategy/shooter games (enemy bots predict & adapt to player moves).
- **Cybersecurity (Adversarial ML)**:
- Defenders (security AI) vs Attackers (malware AI).  
- **Economics / Business**:
- Competitive pricing, bidding, and simulations.
