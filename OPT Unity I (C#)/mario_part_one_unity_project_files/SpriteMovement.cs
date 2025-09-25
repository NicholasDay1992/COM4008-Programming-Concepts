using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using TMPro; // For TextMeshPro

public class NewBehaviourScript : MonoBehaviour
{
    public float moveSpeed = 5f;

    public TextMeshProUGUI collisionText; 

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        // Get horizontal input (-1 for left, 1 for right)
        float horizontalInput = Input.GetAxis("Horizontal");

        // Calculate movement vector
        Vector3 movement = new Vector3(horizontalInput, 0f, 0f) * moveSpeed * Time.deltaTime;

        // Move the sprite
        transform.position += movement;

        //collisionText.text = "player moving";
    }

    void OnCollisionEnter2D(Collision2D collision)
    {
        collisionText.text = "Collided with: " + collision.gameObject.name;
        // Print a message to the Console when a 2D collision occurs
        Debug.Log("Collided with: " + collision.gameObject.name);
    }

}
