using UnityEngine;
using TMPro; // For TextMeshPro

public class MarioJump : MonoBehaviour
{
    private Rigidbody2D rb;
    public float jumpForce = 10f; // Force of the jump
    public LayerMask groundLayer; // Layer representing ground
    public Transform groundCheck; // Empty GameObject to check if on the ground
    public float groundCheckRadius = 0.2f; // Radius of the ground check circle

    private bool isGrounded;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        // Check if Mario is on the ground
        isGrounded = Physics2D.OverlapCircle(groundCheck.position, groundCheckRadius, groundLayer);

        // Jump logic
        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            Jump();
        }
    }

    void Jump()
    {
        rb.velocity = new Vector2(rb.velocity.x, jumpForce); // Apply upward velocity
    }

    private void OnDrawGizmosSelected()
    {
        // Draw ground check radius for debugging
        if (groundCheck != null)
        {
            Gizmos.color = Color.red;
            Gizmos.DrawWireSphere(groundCheck.position, groundCheckRadius);
        }
    }
}