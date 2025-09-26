---

## Minimax Algorithm

- **Introduced**: Early 20th century in Game Theory.  
- **Key Contributor**: John von Neumann (1928) – *Minimax Theorem*.  
- **Adopted in AI**: 1950s onward, especially for Chess programs.  

**Significance**:
- Foundation for **adversarial search** in AI.
- Base for modern **game-playing AI**.

### Core Idea
- Used for **two-player, zero-sum games**.
- **Players**:
  - **MAX** → tries to maximize the score.
  - **MIN** → tries to minimize the score.
- Strategy: *Choose the move that maximizes your minimum gain, assuming the opponent plays optimally.*

### How it Works
1. Construct a **game tree** with all possible moves.
2. **Leaf nodes** → terminal states with evaluation scores.
3. Work upward:
   - **MAX node** picks the maximum child value.
   - **MIN node** picks the minimum child value.
4. **Root’s value** = best decision for the current player.

### Limitation
- Explores *all* possible nodes.  
- **Time complexity**:  
  \[
  O(b^d) \quad \text{where } b = \text{branching factor}, \ d = \text{depth}
  \]

---

## Alpha-Beta Pruning

An optimization of **Minimax** to reduce unnecessary exploration.

### Key Concepts
- **Alpha (α)** → Best value MAX can guarantee so far.  
- **Beta (β)** → Best value MIN can guarantee so far.  
- **Pruning Rule**: If at any point `α ≥ β`, stop exploring that branch.

### Complexity
- **Worst case**: \(O(b^d)\) (same as Minimax).  
- **Best case**: \(O(b^{d/2})\) (dramatic improvement).  

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

---
